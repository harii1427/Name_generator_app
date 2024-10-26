import streamlit as st
import random
import string

male_names = [
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas",
    "Christopher", "Daniel", "Matthew", "George", "Anthony", "Donald", "Paul", "Mark", "Edward", "Steven",
    "Brian", "Kevin", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas",
    "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Frank", "Benjamin", "Gregory",
    "Samuel", "Raymond", "Patrick", "Alexander", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose",
    "Henry", "Adam", "Douglas", "Nathan", "Peter", "Zachary", "Kyle", "Walter", "Harold", "Jeremy",
    "Ethan", "Carl", "Keith", "Roger", "Gerald", "Christian", "Terry", "Sean", "Arthur", "Austin",
    "Noah", "Lawrence", "Jesse", "Joe", "Bryan", "Billy", "Jordan", "Albert", "Dylan", "Bruce",
    "Willie", "Gabriel", "Alan", "Juan", "Logan", "Wayne", "Ralph", "Roy", "Eugene", "Randy",
    "Vincent", "Russell", "Louis", "Philip", "Bobby", "Johnny", "Bradley", "Ricky", "Stanley", "Shawn",
    "Christopher", "Rodney", "Jerry", "Jerry", "Alan", "Rodney", "Jack", "Brandon", "Raymond", "Terry",
    "Adam", "Jordan", "Michael", "Ralph", "Tyler", "Juan", "Kyle", "Albert", "Bobby", "Zachary",
    "Lawrence", "Dennis", "Louis", "Bruce", "Billy", "Walter", "Roy", "Patrick", "Gabriel", "Russell",
    "Stephen", "Eugene", "Jeremy", "Christopher", "Henry", "Frank", "Noah", "Willie", "Christian", "Carl",
    "Dylan", "Keith", "Raymond", "Jacob", "Alan", "Justin", "Roger", "Joe", "Aaron", "Philip",
    "Arthur", "Scott", "Ryan", "Anthony", "Donald", "Douglas", "Sean", "Jonathan", "Eric", "Adam",
    "Mark", "Jacob", "Jesse", "Jack", "Terry", "Raymond", "Gary", "Jerry", "Patrick", "Roger",
    "Rodney", "Eugene", "Harold", "Jeremy", "Dylan", "Raymond", "Tyler", "Jordan", "Austin", "Henry",
    "Juan", "Carl", "Christian", "Alan", "Stephen", "Ralph", "Billy", "Christopher", "Wayne", "Louis",
    "Russell", "Joe", "Terry", "Gabriel", "Kyle", "Ricky", "Willie", "Philip", "Bruce", "Roy",
    "Logan", "Lawrence", "Roger", "Alan", "Billy", "Austin", "Adam", "Jordan", "Louis", "Harold",
    "Patrick", "Jeremy", "Henry", "Russell", "Tyler", "Jacob", "Raymond", "Christian", "Dylan", "Wayne"
]

female_names = [
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
    "Nancy", "Lisa", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna", "Michelle",
    "Dorothy", "Carol", "Amanda", "Melissa", "Deborah", "Stephanie", "Rebecca", "Laura", "Sharon", "Cynthia",
    "Kathleen", "Amy", "Shirley", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Emma", "Samantha",
    "Katherine", "Christine", "Debra", "Rachel", "Catherine", "Carolyn", "Janet", "Ruth", "Maria", "Heather",
    "Diane", "Virginia", "Julie", "Joyce", "Victoria", "Olivia", "Megan", "Martha", "Kelly", "Andrea", "Crystal",
    "Cheryl", "Jacqueline", "Hannah", "Erin", "Sara", "Diana", "Paula", "Christina", "Kathryn", "Evelyn", "Joan",
    "Madison", "Christine", "Alice", "Louise", "Ashley", "Marie", "Julia", "Grace", "Eleanor", "Brittany", "Doris",
    "Phyllis", "Anne", "Natalie", "Amanda", "Jean", "Frances", "Judith", "Rose", "Emma", "Theresa", "Gloria", "Tina",
    "Marie", "Tina", "Catherine", "Judith", "Christina", "Margaret", "Deborah", "Anne", "Gloria", "Emma",
    "Sara", "Kelly", "Jessica", "Emily", "Julia", "Tina", "Patricia", "Alice", "Doris", "Ashley",
    "Heather", "Amanda", "Joyce", "Rachel", "Debra", "Louise", "Martha", "Julie", "Melissa", "Sara", "Rebecca",
    "Sandra", "Angela", "Christine", "Erin", "Helen", "Olivia", "Katherine", "Victoria", "Maria", "Evelyn", "Jean",
    "Nancy", "Phyllis", "Brittany", "Diane", "Brenda", "Sarah", "Jacqueline", "Marie", "Donna", "Kathryn", "Alice",
    "Elizabeth", "Shirley", "Samantha", "Amanda", "Eleanor", "Kelly", "Maria", "Madison", "Crystal", "Paula", "Theresa",
    "Kathleen", "Andrea", "Amy", "Melissa", "Rose", "Deborah", "Tina", "Joan", "Judith", "Margaret", "Frances",
    "Carolyn", "Victoria", "Gloria", "Christine", "Anne", "Louise", "Christina", "Grace", "Doris", "Rachel", "Kelly",
    "Natalie", "Olivia", "Julia", "Heather", "Judith", "Brittany", "Catherine", "Melissa", "Rebecca", "Phyllis", "Amanda"
]

def generate_name(gender, starts_with, length):
    if gender == "Male":
        names = male_names
    elif gender == "Female":
        names = female_names
    else:
        return "Invalid gender"

    filtered_names = [name for name in names if name.startswith(starts_with) and len(name) == length]
    if filtered_names:
        return random.choice(filtered_names)
    else:
        return "No names found with specified constraints"

def main():
    st.title("Name Generator App")

    st.sidebar.subheader("Options")
    gender = st.sidebar.selectbox("Select gender", ["Male", "Female"])
    starts_with = st.sidebar.text_input("Starts with (leave blank for any)", "").capitalize()
    length = st.sidebar.number_input("Length of the name", min_value=1, step=1)

    if st.sidebar.button("Generate Name"):
        name = generate_name(gender, starts_with, length)
        st.success(f"Random {gender} name: {name}")

    # Add some content
    st.header("Welcome to the Name Generator App!")
    st.write("This app allows you to generate random names based on your preferences.")
    st.write("You can specify the gender, starting letter, and length of the name to generate personalized results.")
    st.write("Use the options on the sidebar to customize your search, then click 'Generate Name' to get a random name.")
if __name__ == "__main__":
    main()
