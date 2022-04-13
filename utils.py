import csv
import pandas as pd
import plotly.express as px

def create_csv():
    with open("temperatures.csv", "w", errors="ignore", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["city", "temp", "max_t", "min_t"])


def add_to_csv(city, temp, max_t, min_t):
    with open("temperatures.csv", "a", errors="ignore", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([city, temp, max_t, min_t])


def create_plot():
    df = pd.read_csv("temperatures.csv")
    fig = px.bar(df, x=df["city"], y=["temp", "max_t", "min_t"], title="Temperature")
    fig.show()
    fig.write_image("plot.png")
