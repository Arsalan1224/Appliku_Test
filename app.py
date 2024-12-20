import os

def display_env_variables():
    # Fetch all environment variables
    env_vars = os.environ

    # Print each environment variable and its value
    for key, value in env_vars.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print("Environment Variables in Appliku:")
    display_env_variables()
