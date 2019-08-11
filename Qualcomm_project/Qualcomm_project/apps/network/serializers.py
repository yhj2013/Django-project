from rest_framework import serializers

# from .models import .


class NetworkSerializer(serializers.ModelSerializer):
    """network序列化器"""

    class Meta:
        model = ''  # 这里指定对应的那个数据表