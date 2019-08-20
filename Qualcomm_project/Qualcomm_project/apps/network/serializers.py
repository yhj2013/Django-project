from rest_framework import serializers
from .models import NetworkInfo


# from .models import .


# class NetworkSerializer(serializers.Serializer):
#     """network序列化器"""
#     id = serializers.IntegerField(label='id')
#     country = serializers.StringRelatedField(label='country')
#     operator = serializers.StringRelatedField(label='operator')
#     city = serializers.CharField(label='city', required=False)
#     city_num = serializers.IntegerField(label='city_num', required=False)
#     launch_date = serializers.DateField(label='launch_date', required=False)
#     launch_date_year = serializers.CharField(label='launch_date_year', required=False)
#     num_sites_first_launch_nsa = serializers.IntegerField(label='num_sites_first_launh_nsa', required=False)
#     num_sites_first_launch_nsa_notes = serializers.CharField(label='num_sites_first_launch_nsa_notes', required=False)
#     num_sites_first_launch_sa = serializers.IntegerField(label='num_sites_first_launch_sa', required=False)
#     num_cities_first_launch = serializers.IntegerField(label='num_cities_first_launch', required=False)
#     num_cities_first_launch_notes = serializers.CharField(label='num_cities_first_alunh_notes', required=False)
#     deployment_type = serializers.CharField(label='deployment_type', required=False)
#     frequency_band = serializers.CharField(label='frenquency_band', required=False)
#     bandwidth = serializers.CharField(label='bandwidth', required=False)
#     frequency = serializers.CharField(label='frequency', required=False)
#     number_of_subscribers = serializers.CharField(label='number_of_subscribers', required=False)
#     active_antenna_used = serializers.CharField(label='active_antenna_used', required=False)
#     infra_vendor_radio = serializers.CharField(label='infra_vendor_radio', required=False)
#     infra_vendor_core = serializers.CharField(label='infra_vendor_core', required=False)
#     data_source = serializers.CharField(label='data_source', required=False)
#     notes = serializers.CharField(label='notes', required=False)
#     technology = serializers.CharField(label='technology', required=False)
#     band_type = serializers.CharField(label='band_type', required=False)
#     infra_vendor_radio_first = serializers.CharField(label='infra_vendor_radio_first', required=False)
#     data_update_date = serializers.DateField(label='data_update_date', required=False)


class NetworkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')

    class Meta:
        model = NetworkInfo
        fields = '__all__'


class UpdateNetworkSerializer(serializers.Serializer):
    country_id = serializers.IntegerField(label='country', required=False)
    operator_id = serializers.IntegerField(label='operator', required=False)
    city = serializers.CharField(label='city', required=False)
    city_num = serializers.IntegerField(label='city_num', required=False)
    launch_date = serializers.DateField(label='launch_date', required=False)
    launch_date_year = serializers.CharField(label='launch_date_year', required=False)
    num_sites_first_launch_nsa = serializers.IntegerField(label='num_sites_first_launh_nsa', required=False)
    num_sites_first_launch_nsa_notes = serializers.CharField(label='num_sites_first_launch_nsa_notes', required=False)
    num_sites_first_launch_sa = serializers.IntegerField(label='num_sites_first_launch_sa', required=False)
    num_cities_first_launch = serializers.IntegerField(label='num_cities_first_launch', required=False)
    num_cities_first_launch_notes = serializers.CharField(label='num_cities_first_alunh_notes', required=False)
    deployment_type = serializers.CharField(label='deployment_type', required=False)
    frequency_band = serializers.CharField(label='frenquency_band', required=False)
    bandwidth = serializers.CharField(label='bandwidth', required=False)
    frequency = serializers.CharField(label='frequency', required=False)
    number_of_subscribers = serializers.CharField(label='number_of_subscribers', required=False)
    active_antenna_used = serializers.CharField(label='active_antenna_used', required=False)
    infra_vendor_radio = serializers.CharField(label='infra_vendor_radio', required=False)
    infra_vendor_core = serializers.CharField(label='infra_vendor_core', required=False)
    data_source = serializers.CharField(label='data_source', required=False)
    notes = serializers.CharField(label='notes', required=False)
    technology = serializers.CharField(label='technology', required=False)
    band_type = serializers.CharField(label='band_type', required=False)
    infra_vendor_radio_first = serializers.CharField(label='infra_vendor_radio_first', required=False)
    data_update_date = serializers.DateField(label='data_update_date', required=False)

    def update(self, instance, validated_data):

        instance.country_id = validated_data.get('country_id', instance.country_id)
        instance.operator_id = validated_data.get('operator_id', instance.operator_id)
        instance.city = validated_data.get('city', instance.city)
        instance.city_num = validated_data.get('city_num', instance.city_num)
        instance.launch_date = validated_data.get('launch_date', instance.launch_date)
        instance.launch_date_year = validated_data.get('launch_date', instance.launch_date)
        instance.num_sites_first_launch_nsa = validated_data.get('num_sites_first_launch_nsa', instance.num_sites_first_launch_nsa)
        instance.num_sites_first_launch_nsa_notes = validated_data.get('num_sites_first_launch_nsa_notes', instance.num_sites_first_launch_nsa_notes)
        instance.num_sites_first_launch_sa = validated_data.get('num_sites_first_launch_sa', instance.num_sites_first_launch_sa)
        instance.num_cities_first_launch = validated_data.get('num_cities_first_launch', instance.num_cities_first_launch)
        instance.num_cities_first_launch_notes = validated_data.get('num_cities_first_launch_notes', instance.num_cities_first_launch_notes)
        instance.deployment_type = validated_data.get('deployment_type', instance.deployment_type)
        instance.frequency_band = validated_data.get('frequency_band', instance.frequency_band)
        instance.bandwidth = validated_data.get('bandwidth', instance.bandwidth)
        instance.frequency = validated_data.get('frequency', instance.frequency)
        instance.number_of_subscribers = validated_data.get('number_of_subscribers', instance.number_of_subscribers)
        instance.active_antenna_used = validated_data.get('active_antenna_used', instance.active_antenna_used)
        instance.infra_vendor_radio = validated_data.get('infra_vendor_radio', instance.infra_vendor_radio)
        instance.infra_vendor_core = validated_data.get('infra_vendor_core', instance.infra_vendor_core)
        instance.data_source = validated_data.get('data_source', instance.data_source)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.technology = validated_data.get('technology', instance.technology)
        instance.band_type = validated_data.get('band_type', instance.band_type)
        instance.infra_vendor_radio_first = validated_data.get('infra_vendor_radio_first', instance.infra_vendor_radio_first)
        instance.data_update_date = validated_data.get('data_update_date', instance.data_update_date)
        instance.save()
        print('success')


        return instance
