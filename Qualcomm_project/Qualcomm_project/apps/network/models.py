from django.db import models


# Create your models here.

class CountryGsmaInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    country = models.TextField(blank=True, null=True, verbose_name='country')
    region = models.TextField(blank=True, null=True, verbose_name='region')
    subregion = models.TextField(blank=True, null=True, verbose_name='subregion')
    iso = models.TextField(blank=True, null=True, verbose_name='iso')

    class Meta:
        managed = True
        db_table = 'country_gsma'
        verbose_name = 'country_gsma'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.country


class OperatorGsmaInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    country = models.TextField(blank=True, null=True, verbose_name='country')
    operator = models.TextField(blank=True, null=True, verbose_name='operator')
    pmn = models.TextField(blank=True, null=True, verbose_name='pmn')
    url = models.TextField(blank=True, null=True, verbose_name='url')
    status = models.TextField(blank=True, null=True, verbose_name='status')
    launch_date = models.DateTimeField(db_column='launch date', blank=True, null=True,
                                       verbose_name='launch_date')  # Field renamed to remove unsuitable characters.
    country_01 = models.ForeignKey('CountryGsmaInfo', on_delete=models.CASCADE, blank=True, db_column='country_id',
                                   null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = True
        db_table = 'operator_gsma'
        verbose_name = 'operator_gsma'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.operator


# -----------------------------------site schema-----------------------------------------------------------------------------


class NetworkInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    # country = models.ForeignKey('CountryGsmaInfo', on_delete=models.CASCADE, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    # operator = models.ForeignKey('OperatorGsmaInfo', on_delete=models.CASCADE, blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name='city')
    city_num = models.IntegerField(blank=True, null=True, verbose_name='city_num')
    launch_date = models.DateField(blank=True, null=True, verbose_name='launch_date')
    launch_date_year = models.CharField(max_length=200, blank=True, null=True, verbose_name='launch_data_year')
    num_sites_first_launch_nsa = models.IntegerField(blank=True, null=True, verbose_name='num_sites_first_launch_nsa')
    num_sites_first_launch_nsa_notes = models.CharField(max_length=200, blank=True, null=True,
                                                        verbose_name='num_sites_first_launh_nsa_notes')
    num_sites_first_launch_sa = models.IntegerField(blank=True, null=True, verbose_name='num_sites_first_launch_sa')
    num_cities_first_launch = models.IntegerField(blank=True, null=True, verbose_name='num_cities_first_launch')
    num_cities_first_launch_notes = models.CharField(max_length=200, blank=True, null=True,
                                                     verbose_name='num_cities_first_launch_notes')
    deployment_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='deployment')
    frequency_band = models.CharField(max_length=200, blank=True, null=True, verbose_name='frequency_band')
    bandwidth = models.CharField(max_length=200, blank=True, null=True, verbose_name='bandwidth')
    frequency = models.CharField(max_length=200, blank=True, null=True, verbose_name='frequency')
    number_of_subscribers = models.CharField(max_length=200, blank=True, null=True,
                                             verbose_name='number_of_subscribers')
    active_antenna_used = models.CharField(max_length=200, blank=True, null=True, verbose_name='active_antenna_used')
    infra_vendor_radio = models.CharField(max_length=200, blank=True, null=True, verbose_name='infra_vendor_radio')
    infra_vendor_core = models.CharField(max_length=200, blank=True, null=True, verbose_name='infra_vendor_core')
    data_source = models.CharField(max_length=200, blank=True, null=True, verbose_name='data_source')
    notes = models.CharField(max_length=200, blank=True, null=True, verbose_name='notes')
    technology = models.CharField(max_length=200, blank=True, null=True, verbose_name='technology')
    band_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='band_type')
    infra_vendor_radio_first = models.CharField(max_length=200, blank=True, null=True,
                                                verbose_name='infra_vendor_radio_first')
    data_update_date = models.DateField(blank=True, null=True, verbose_name='data_update_date')

    class Meta:
        managed = True

        db_table = 'network'
        verbose_name = 'network'
        verbose_name_plural = verbose_name
