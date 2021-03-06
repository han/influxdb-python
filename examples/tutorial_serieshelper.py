from influxdb import InfluxDBClient
from influxdb import SeriesHelper


class MySeriesHelper(SeriesHelper):
    class Meta:
        # Meta class stores time series helper configuration.
        client = InfluxDBClient()
        # The client should be an instance of InfluxDBClient.
        series_name = 'events.stats.{server_name}'
        # The series name must be a string. Add dependent field names in curly brackets.
        fields = ['time', 'server_name']
        # Defines all the fields in this time series.
        bulk_size = 5
        # Defines the number of data points to store prior to writing on the wire.

# The following will create *five* (immutable) data points.
# Since bulk_size is set to 5, upon the fifth construction call, *all* data
# points will be written on the wire via MySeriesHelper.Meta.client.
MySeriesHelper(server_name='us.east-1', time=159)
MySeriesHelper(server_name='us.east-1', time=158)
MySeriesHelper(server_name='us.east-1', time=157)
MySeriesHelper(server_name='us.east-1', time=156)
MySeriesHelper(server_name='us.east-1', time=155)

# To manually submit data points which are not yet written, call commit:
MySeriesHelper.commit()

# To inspect the JSON which will be written, call _json_body_():
MySeriesHelper._json_body_()
