"""
# ------------------------------------------------
# Program:
#       This project is used to check the certificate expired date & trigger the certificate renewal pipeline in Jenkins
#       此项目用于检查证书过期日期并在Jenkins触发证书更新流水线
# History:
#       11/10/2024 周月南 First release
# ------------------------------------------------
"""
import jenkins
import socket
import ssl
from datetime import datetime, timedelta


class Certificate:
    def __init__(self) -> None:
        self.notBefore = None
        self.notAfter = None
        self.countryName = None

    def obtain_certificate_expired_time(self, domain: str) -> str:
        """
        This function is used to obtain the certificate expired time by domain name
        :param domain: This parameter is used to define the domain name
        :return: Return the certificate expire time of string type
        """
        hostname = domain
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print(ssock.version())
                certificate_details = ssock.getpeercert()
                print(certificate_details)
                self.notBefore = certificate_details['notBefore']
                self.notAfter = certificate_details['notAfter']
                print(f"The certificate issued time is: {certificate_details['notBefore']}")
                print(f"The certificate expired time is {certificate_details['notAfter']}")
                for i in range(len(certificate_details['subject'])):
                    print(certificate_details['subject'][i][0][0])
                    if certificate_details['subject'][i][0][0] in 'countryName':
                        print(f"The certificate country name is {certificate_details['subject'][i][0][1]}")
                        self.countryName = certificate_details['subject'][i][0][1]
                        print(self.countryName, self.notBefore, self.notAfter)

        return certificate_details['notAfter']

    @staticmethod
    def time_type_calculation(time_datetime) -> datetime:
        """
        This function is used to calculate the expired date for the certificate
        :param time_datetime:
        :return: Return the certificate validity date
        """
        remaining_time = time_datetime - datetime.utcnow()
        print(remaining_time)
        if remaining_time < timedelta(days=30):
            pass
        return remaining_time


    @staticmethod
    def time_type_conversion(time_str: str) -> datetime:
        """
        This function is used to convert the certificate type from string type to datetime type
        :param time_str: Thus parameter is used to define the time of string type
        :return: Return the time of datatime type
        """
        time_str_conversion = time_str
        date_time = datetime.strptime(time_str_conversion, "%b %d %H:%M:%S %Y GMT")
        print(time_str_conversion)
        print(date_time)
        return date_time

    def trigger_jenkins_pipeline(self, job) -> None:
        """
        This function is used to trigger the Jenkins pipeline to make the certificate
        :param job: This parameter is used to define the Jenkins job name
        :return: Return None
        """
        connection = jenkins.Jenkins("http://47.109.56.146:32000/", "zhouyuenan", "zyb19990712")
        try:
            connection.build_job(job, {"Domain_Name": self.notBefore, "Country": self.countryName})
            print(self.notAfter, self.countryName)
        except NameError as e:
            print(e)

if __name__ == '__main__':
    certificate = Certificate()
    time_str_type = certificate.obtain_certificate_expired_time(domain="www.baidu.com")
    time_datetime_type = certificate.time_type_conversion(time_str=time_str_type)
    certificate.time_type_calculation(time_datetime_type)
    certificate.trigger_jenkins_pipeline("Test")




