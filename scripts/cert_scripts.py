from scripts.tools import get_account
from scripts.user_data import user_data
from brownie import Certificate
from brownie import Contract
from PIL import Image, ImageDraw, ImageFont
import requests
import json

status = []


def get_account_list():
    for i in range(9):
        account = get_account(i + 1)
        print(account)


def deploy_contract():
    account = get_account()
    certificate = Certificate.deploy(
        "Federation of Esports Associations India", "BIT", {"from": account}
    )
    deployed_contract = {"deployed_contract": certificate.address}
    with open("deployed_contract.json", "w") as file:
        json.dump(deployed_contract, file)


def prepare_cert_images():
    for user in user_data:
        print_image(user["user_name"], user["tournament_name"], user["user_account"])


def print_image(name, tournament, account):
    image = Image.open("template.jpeg")
    I1 = ImageDraw.Draw(image)
    myFont = ImageFont.truetype("arial.ttf", 40)
    x_pos = 450
    I1.text((x_pos, 420), name, font=myFont, fill=(0, 0, 0))
    myFont = ImageFont.truetype("arial.ttf", 18)
    x_pos = 820
    I1.text((x_pos, 500), tournament, font=myFont, fill=(0, 0, 0))
    image.show()
    image.save("certificates/" + account + ".png")


def upload_certificate(account):
    url = "https://api.web3.storage/upload"
    filepath = "certificates/" + account + ".png"
    files = {"file": open(filepath, "rb")}
    response = requests.post(
        url,
        files=files,
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGQyRjVFZkI5QmZFOThhOGQ4YkQ0NzVmMTg4OTU5N2YxQ2M2QzBiMkIiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NTg0OTc1NzYxNzksIm5hbWUiOiJibG9rY3JlZCJ9.VwdALjKL1nRP9uiKkjlAnDcK7x2_RZi-28viJ4sXNgU"
        },
    )
    cid = response.json()["cid"]
    file_url = "http://" + cid + ".ipfs.dweb.link"
    return file_url


def upload_metadata(account):
    url = "https://api.web3.storage/upload"
    filepath = "metadata/" + account + ".json"
    files = {"file": open(filepath, "rb")}
    response = requests.post(
        url,
        files=files,
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGQyRjVFZkI5QmZFOThhOGQ4YkQ0NzVmMTg4OTU5N2YxQ2M2QzBiMkIiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NTg0OTc1NzYxNzksIm5hbWUiOiJibG9rY3JlZCJ9.VwdALjKL1nRP9uiKkjlAnDcK7x2_RZi-28viJ4sXNgU"
        },
    )
    cid = response.json()["cid"]
    file_url = "http://" + cid + ".ipfs.dweb.link"
    return file_url


def create_metadata(name, tournament, account, cert_url):
    nft_name = "Certificate of Participation"
    nft_description = f"Certificate of participation proudly presented to {name} and this certifies that he/she has participated in {tournament} in IRIS RANBHOOMI 2022 held at Indian institute of Management, Indore from November 11, 2022 - November 13, 2022"
    metadata = {"name": nft_name, "description": nft_description, "image": cert_url}
    metadata_filepath = "metadata/" + account + ".json"
    with open(metadata_filepath, "w") as metadata_file:
        json.dump(metadata, metadata_file)
    metadata_url = upload_metadata(account)
    return metadata_url


def mint_certificates():
    with open("build/contracts/Certificate.json", "r") as file:
        data = json.load(file)
        abi = data["abi"]
    with open("deployed_contract.json", "r") as file:
        data = json.load(file)
        deployed_contract = data["deployed_contract"]
    certificate = Contract.from_abi("Certificate", deployed_contract, abi)
    for user in user_data:
        user_status = {"name": user["user_name"], "account": user["user_account"]}
        try:
            cert_url = upload_certificate(account=user["user_account"])
            user_status["cert_url"] = cert_url
            metadata_url = create_metadata(
                user["user_name"],
                user["tournament_name"],
                user["user_account"],
                cert_url,
            )
            user_status["metadata_url"] = metadata_url
            account = get_account()
            certificate_creation_tx = certificate.createCertificate(
                metadata_url, user["user_account"], {"from": account}
            )
            certificate_creation_tx.wait(1)
            user_status["status"] = "Success"
        except:
            user_status["status"] = "Failed"
        status.append(user_status)
    with open("status.json", "w") as status_file:
        json.dump(status, status_file)


def check_issued_certificates():
    with open("build/contracts/Certificate.json", "r") as file:
        data = json.load(file)
        abi = data["abi"]
    certificate = Contract.from_abi(
        "Certificate", "0x1F18686Df440E13Ad95AeF3fd8E572bDA8c69872", abi
    )
    mint_status = {}
    for user in user_data:
        user_address = user["user_account"]
        balance = certificate.balanceOf(user_address)
        if int(balance) == 1:
            mint_status[user_address] = "Success"
        elif int(balance) == 0:
            mint_status[user_address] = "Failed"
        elif int(balance) > 1:
            mint_status[user_address] = "ooooooooooooppppppppsssssssssssss"
    print(mint_status)
