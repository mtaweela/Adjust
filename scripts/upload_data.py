

class DataUploader:
    from dataRestApp import models
    file = ''

    def add_Channels(self):
        from csv import reader
        with open(self.file, 'rb') as f:
            csv_reader = reader(f, delimiter=',')
            for row_index, row in enumerate(csv_reader):
                if row_index != 0:
                    channel_name = row[1]
                    try:
                        new_channel = self.models.AdvertisingChannel.objects.create(
                            name=channel_name)
                    except Exception as e:
                        pass

    def add_Countriess(self):
        from csv import reader
        with open(self.file, 'rb') as f:
            csv_reader = reader(f, delimiter=',')
            for row_index, row in enumerate(csv_reader):
                if row_index != 0:
                    country_name = row[2]
                    try:
                        country = self.models.Country.objects.create(
                            name=country_name)
                    except Exception as e:
                        pass

    def add_OperatingSystems(self):
        from csv import reader
        with open(self.file, 'rb') as f:
            csv_reader = reader(f, delimiter=',')
            for row_index, row in enumerate(csv_reader):
                if row_index != 0:
                    os_name = row[3]
                    try:
                        new_os = self.models.OperatingSystem.objects.create(
                            name=os_name)
                    except Exception as e:
                        pass

    def add_PerformanceMetrics(self):
        from csv import reader
        with open(self.file, 'rb') as f:
            csv_reader = reader(f, delimiter=',')
            for row_index, row in enumerate(csv_reader):
                if row_index != 0:
                    advertising_channel = self.models.AdvertisingChannel.objects.get(
                        name=row[1])
                    country = self.models.Country.objects.get(
                        name=row[2])
                    operating_system = self.models.OperatingSystem.objects.get(
                        name=row[3])

                    date = row[0]
                    impressions = row[4]
                    clicks = row[5]
                    installs = row[6]
                    spend = row[7]
                    revenue = row[8]

                    f_date = row[0].split('.')
                    f_date = [f_date[2], f_date[1], f_date[0]]
                    date = '-'.join(f_date)
                    try:
                        performanceMetric = self.models.PerformanceMetric.objects.create(
                            impressions=impressions,
                            clicks=clicks,
                            installs=installs,
                            spend=spend,
                            revenue=revenue,
                            date=date,
                            advertising_channel=advertising_channel,
                            country=country,
                            operating_system=operating_system
                        )
                        print performanceMetric
                    except Exception as e:
                        print e
                        pass

    def add_all_data_to_db(self):
        self.add_Channels()
        self.add_Countriess()
        self.add_OperatingSystems()
        self.add_PerformanceMetrics()
        print "FINISHED ALL....."


data_uploader = DataUploader()
data_uploader.file = './dataset.csv'
data_uploader.add_all_data_to_db()
