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
    @staticmethod
    def obtain_certificate_expired_time(domain: str) -> str:
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
                print(f"The certificate issued time is: {certificate_details['notBefore']}")
                print(f"The certificate expired time is {certificate_details['notAfter']}")
        return certificate_details['notAfter']

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

    @staticmethod
    def time_type_calculation(time_datetime) -> datetime:
        """
        This function is used to calculate the expired date for the certificate
        :param time_datetime:
        :return:
        """
        remaining_time = time_datetime - datetime.utcnow()
        print(remaining_time)
        if remaining_time < timedelta(days=30):
            pass
        return None

    @staticmethod
    def trigger_Jenkins_pipeline(job) -> None:
        """

        :param job:
        :return:
        """
        connection = jenkins.Jenkins("http://47.109.56.146:32000/", "zhouyuenan", "zyb19990712")
        connection.build_job(job)

if __name__ == '__main__':
    certificate = Certificate()
    time_str_type = certificate.obtain_certificate_expired_time(domain="gitee.com")
    time_datetime_type = certificate.time_type_conversion(time_str=time_str_type)
    certificate.time_type_calculation(time_datetime_type)
    certificate.trigger_Jenkins_pipeline("Test1")
# {'subject': ((('countryName', 'ID'),),
#              (('stateOrProvinceName', 'Daerah Khusus Ibukota Jakarta'),),
#              (('localityName', 'Jakarta Selatan'),),
#              (('organizationName', 'PT AIA  Financial'),),
#              (('commonName', 'irecruit.aia.id'),)),
#  'issuer': ((('countryName', 'US'),),
#             (('organizationName', 'DigiCert Inc'),),
#             (('commonName', 'DigiCert Global G2 TLS RSA SHA256 2020 CA1'),)),
#  'version': 3,
#  'serialNumber': '0EF872466C2978D2C5C620E85371C555',
#  'notBefore': 'May 14 00:00:00 2024 GMT',
#  'notAfter': 'May 13 23:59:59 2025 GMT',
#  'subjectAltName': (('DNS', 'irecruit.aia.id'),),
#  'OCSP': ('http://ocsp.digicert.com',),
#  'caIssuers': ('http://cacerts.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crt',),
#  'crlDistributionPoints': ('http://crl3.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crl',
#                            'http://crl4.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crl')}



