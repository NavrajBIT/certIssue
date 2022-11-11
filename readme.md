1.  Clone the repository

2.  Prepare a virtual environment
    * >>> mkvirtaulenv . ENV_NAME
    * >>> workon ENV_NAME

3.  install brownie and PIL
    * >>> pip install eth-brownie
    * >>> pip install PIL

4.  * open "data.xlsx" file and input the data.
    * Yellow cells are input fields.

5.  * Copy the input data from "data.xlsx" to "scripts/user_data.py" file.
    * The green cells are "data.xlsx" file are to be copied at once and paste in "scripts/user_data.py" file.

6.   Create a .env file and fill in the private key or network details.

7.  * Run the issue_all.py file.
    * >>> brownie run scripts/issue_all.py
    * run in local environment for practice.

8.  Check the status from "status.json" file or run check_status.py file
    * >>> brownie run scripts/check_status.py

9. Modify the user_data.py file by deleting the successful enteries.

10. rerun the minting script from mint_certs.py file
    * >>> brownie run scripts/mint_certs.py

11.  Change the the brownie network to polygon and run step 7.
    * >>>brownie networks add Polygon polygon-mainnet host=https://rplurl chainid=137
    * >>>brownie run scripts/issue_all.py --network polygon-mainnet

12.  Check the status from "status.json" file.



