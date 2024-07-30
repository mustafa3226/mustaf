import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent,Task,Crew,Process
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from faker import Faker
from crewai_tools import tool
import csv
import random
os.environ['SERPER_API_KEY'] = '3632f07df24cfb1fe528e0d73de7e3e26dd88eb2'
Google_api_key=os.getenv('GEMINI_API_KEY')
Open_api_key=os.getenv('OPENAI_API_KEY')
LLM=ChatGoogleGenerativeAI(model='gemini-1.5-flash',temperature=0.5,verbose=True,google_api_key=Google_api_key)
fake=Faker()

universities = [
    "Harvard University", 
    "Stanford University", 
    "MIT", 
    "University of Cambridge", 
    "University of Oxford",
    "California Institute of Technology",
    "Princeton University",
    "Yale University",
    "University of Chicago",
    "Columbia University"
]
@tool
def generate_random_data(num_records=10):
    """
    Generates random user data including name, age, and city.
    
    Args:
        num_records (int): Number of records to generate. Default is 10.
    
    Returns:
        list: A list of dictionaries containing random user data.
    """
    data = []
    for _ in range(num_records):
        data.append({
            'Name': fake.name(),
            'Age': fake.random_int(min=18,max=24),
            'City': fake.city(),
            'university':random.choice(universities)
            
            })
    return data
@tool
def write_to_csv(data, filename='random_data.csv'):
    """
    Writes the provided data to a CSV file.
    
    Args:
        data (list): List of dictionaries containing data to write.
        filename (str): Name of the CSV file to write to. Default is 'random_data.csv'.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

