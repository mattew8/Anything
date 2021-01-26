from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from BlogApp.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        owner = serializers.ReadOnlyField(source='owner.username')
        # ReadOnlyField? -> 그냥 Charfield(read_only=True)랑 같은 역할
        # source를 통해 field 채울 내용 정함
        fields = ('id', 'title', 'content', 'owner',)


# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
    # 유효성 검사 된 데이터(validated_data)를 기반으로 객체 인스턴스를 반환하려면 .create(), .update()중 하나를 구현해야!
    # 지금은 create를 오버라이딩 해준 것
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


# 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    # 왜? Post는 현재 User와 역참조 관계! serializer에서 자동으로 추가x
    # so 명백히 선언해줄 필요! -> model의 owner필드에서 설정한 related_name 속성으로 찾아낼 수 o

    class Meta:
        model = User
        fields = ("id", "username", "post")


# 로그인
class LoginUserSerializer(serializers.Serializer):
    # 연결되는 모델x -> 그냥 Serializer로 생성
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # validator 커스텀시 오버라이딩!

        user = authenticate(**data)
        # auth 패키지의 authenticate()함수 사용. AUTH_USER_MODEL(여기서는 User)에서 username가져와 password비교
        # 얘네는 위에서 serializers로 정의!

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")
        # raise -> 얘로 예외 발생 시 raise 아래의 코드는 실행되지 않고 바로 except로 넘어감
