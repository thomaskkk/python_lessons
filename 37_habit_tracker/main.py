import requests
import datetime as dt

API_URL = "https://pixe.la/v1/users"
USERNAME = "" # your desired username here
TOKEN = "" # your generated token here
GRAPH_ID = "graph1"

# Create user ----------------------
def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    r = requests.post(url=API_URL, json=user_params)
    r.raise_for_status()
    print(r.text)

# Create graph ----------------------
def create_graph():
    graph_endpoint = f"{API_URL}/{USERNAME}/graphs"

    graph_config = {
        "id": GRAPH_ID,
        "name": "Code Graph",
        "unit": "commit",
        "type": "int",
        "color": "sora",
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    r.raise_for_status()
    print(r.text)

# Create pixel ----------------------
def post_pixel():
    post_pixel_endpoint = f"{API_URL}/{USERNAME}/graphs/{GRAPH_ID}"

    pixel_config = {
        "date": dt.datetime.now().strftime('%Y%m%d'),
        "quantity": input("How many commits you did today?"),
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    r = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
    r.raise_for_status()
    print(r.text)

# Update pixel ----------------------
def update_pixel():
    update_pixel_endpoint = f"{API_URL}/{USERNAME}/graphs/{GRAPH_ID}/{dt.datetime.now().strftime('%Y%m%d')}"

    update_pixel_config = {
        "quantity": input("How many commits you want to update today's pixels?"),
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    r = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
    r.raise_for_status()
    print(r.text)

# Delete pixel ----------------------
def delete_pixel():
    delete_pixel_endpoint = f"{API_URL}/{USERNAME}/graphs/{GRAPH_ID}/20241003"

    headers = {
        "X-USER-TOKEN": TOKEN
    }
    r = requests.delete(url=delete_pixel_endpoint, headers=headers)
    r.raise_for_status()
    print(r.text)


options = {
    "user": create_user,
    "graph": create_graph,
    "post": post_pixel,
    "update": update_pixel,
    "delete": delete_pixel,
}
choice = input("What you want to do today? Type the keyword.\nCreate 'user'\nCreate 'graph'\n'post' a pixel\n'update' a pixel\n'delete' a pixel\nType the keyword: ").lower()
options[choice]()