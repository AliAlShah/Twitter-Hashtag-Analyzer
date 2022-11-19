import matplotlib.pyplot as plt

#Function to create bar plot
def plot(posititve, neutral, negative):
    data = {'positive':posititve, "neautral":neutral, "negative":negative}
    labels = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 5))

    plt.bar(labels, values, width=0.4)
    plt.xlabel("Sentiment")
    plt.ylabel("Number of sentiments")
    plt.show()

#Function to create Pie Plot
def pieplot(posititve, neutral, negative):
    plt.pie([posititve, negative, neutral], labels=["Positive", "Negative", "Neutral"])
    plt.show()