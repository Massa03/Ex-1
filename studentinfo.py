import requests

#API
url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

#JSON format
data = {
    "UCID": "mb287",
    "first_name": "Massa",
    "last_name": "Belal",
    "github_username": "Massa03",
    "discord_username": "sea018355",
    "favorite_cartoon": "Tom and Jerry",
    "favorite_language": "Python",
    "movie_or_game_or_book": "La La Land",
    "section": "103"
}

try:
    response = requests.post(url, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
