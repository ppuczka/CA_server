from datetime import datetime, timedelta

from cryptography import x509
from cryptography.hazmat.backends import default_backend

from cryptography.x509.oid import NameOID

from cryptography.hazmat.primitives import hashes, serialization


def generate_public_key(private_key, filename, **kwargs):
    subject = x509.Name(

        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, kwargs["country"]),
            x509.NameAttribute(
                NameOID.STATE_OR_PROVINCE_NAME, kwargs["state"]
            ),
            x509.NameAttribute(NameOID.LOCALITY_NAME, kwargs["locality"]),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, kwargs["org"]),
            x509.NameAttribute(NameOID.COMMON_NAME, kwargs["hostname"]),
        ]
    )

    issuer = subject
    valid_from = datetime.utcnow()
    valid_to = valid_from + timedelta(days=30)

    builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(valid_from)
        .not_valid_after(valid_to)
    )

    public_key = builder.sign(
       private_key, hashes.SHA256(), default_backend()
    )

    with open(filename, "wb") as certfile:
        certfile.write(public_key.public_bytes(serialization.Encoding.PEM))

    return public_key
