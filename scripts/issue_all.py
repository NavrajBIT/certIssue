from scripts.cert_scripts import (
    prepare_cert_images,
    deploy_contract,
    mint_certificates,
    check_issued_certificates,
)


def main():
    prepare_cert_images()
    deploy_contract()
    mint_certificates()
    check_issued_certificates()
