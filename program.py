import requests
import csv
url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"Software developer summer 2024, Toronto","page":"1","num_pages":"1","employment_types":"intern"}

headers = {
	"X-RapidAPI-Key": "415a0a6be1msh02aeb4182630329p1f3d90jsn458dd2fcc06b",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:

    data = response.json().get("data",[])

    jobs = []

    for job in data:
        job_data = {
            "employer_name": job.get("employer_name", ""),
            "job_title": job.get("job_title", ""),
            "job_apply_link": job.get("job_apply_link", ""),
            "job_description": job.get("job_description", "")
        }

        jobs.append(job_data)


    for job in jobs:
        print(job)
        print("\n")


    csv_file = "output.csv"

    with open(csv_file, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["employer_name", "job_title", "job_apply_link", "job_description"]
        writeFields = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writeFields.writeheader()

        for job in jobs:
            writeFields.writerow(job)
else:
    print(f"Error: status code - {response.status_code}")