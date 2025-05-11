import requests
import json

def generate_webhook():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "Md Siddique Abbasi",
        "regNo": "0827CI221090",
        "email": "mdsiddique220460@acropolis.in"
    }
    response = requests.post(url, json=payload)
    return response.json()

def solve_sql_query():
    return """
    SELECT 
        e1.EMP_ID,
        e1.FIRST_NAME,
        e1.LAST_NAME,
        d.DEPARTMENT_NAME,
        COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
    FROM 
        EMPLOYEE e1
    JOIN 
        DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
    LEFT JOIN 
        EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT
                   AND e2.DOB > e1.DOB
    WHERE 
        e1.EMP_ID != e2.EMP_ID
    GROUP BY 
        e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
    ORDER BY 
        e1.EMP_ID DESC;
    """

def submit_solution(webhook_url, access_token, sql_query):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    payload = {
        "finalQuery": sql_query
    }
    response = requests.post(webhook_url, headers=headers, json=payload)
    return response.status_code, response.text

def main():
    webhook_data = generate_webhook()
    webhook_url = webhook_data.get("webhook")
    access_token = webhook_data.get("accessToken")
    
    sql_query = solve_sql_query()
    
    if webhook_url and access_token:
        status_code, response_text = submit_solution(webhook_url, access_token, sql_query)
        print(f"Response Status Code: {status_code}")
        print(f"Response Text: {response_text}")
    else:
        print("Failed to get webhook URL or access token.")

if __name__ == "__main__":
    main()
