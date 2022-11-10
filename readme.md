Step1.
    Clone the repository

Step2.
    Prepare a virtual environment
    >>> mkvirtaulenv . ENV_NAME
    >>> workon ENV_NAME

Step3. 
    install brownie and PIL
    a) >>> pip install eth-brownie
    b) >>> pip install PIL

Step4.
    open "data.xlsx" file and input the data.
    Yellow cells are input fields.

Step5.
    Copy the input data from "data.xlsx" to "scripts/user_data.py" file.
    The green cells are "data.xlsx" file are to be copied at once and paste in "scripts/user_data.py" file.

Step6.
    Create a .env file and fill in the private key or network details.

Step7.
    Run the deploy.py file.
    >>> brownie run scripts/deploy.py
    run in local environment for practice.

Step8.
    Change the the brownie network to polygon and run step 7.

Step9.
    Check the status from "status.json" file.



