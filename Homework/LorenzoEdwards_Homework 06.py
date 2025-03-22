{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lorenzo Edwards"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objective:\n",
    "The objective of this assignment is to practice using Functional Programing.\n",
    "\n",
    "## Instructions:\n",
    "\n",
    "Using everything we learned to day about Functional Programing, lambda and itters create one of each of the following:\n",
    "-  Basic Lambda Function\n",
    "    - Create a lambda function that takes one arguments and returns even or odd.\n",
    "- Advanced lambda Function\n",
    "    - Create a lambda function that takes a list and returns their sum \n",
    "- Sorting with Lambda\n",
    "- Filtering with Lambda - `filter()` \n",
    "- Mapping with Lambda - `map()`\n",
    "- Reducing with Lambda -  `reduce()` \n",
    "- Enumerate with or without Lambda - `enumerate()`\n",
    "- zip with or without lambda (may combine enumerate like in class) - `zip()`\n",
    "\n",
    "Submit the file as a .py \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Odd\n"
     ]
    }
   ],
   "source": [
    "#Function to check if it's even or odd\n",
    "even_or_odd = lambda x: \"Even\" if x % 2 == 0 else \"Odd\"\n",
    "\n",
    "#the actual odd or even differentiation\n",
    "result = even_or_odd(7)\n",
    "\n",
    "#result\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "#Function to sum a list\n",
    "sum_list = lambda lst: sum(lst)\n",
    "\n",
    "#The numbers used\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "#The calculated part\n",
    "result = sum_list(numbers)\n",
    "\n",
    "#The result\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "#First I'll have the list of numbers\n",
    "numbers = [4, 1, 7, 3, 9, 2]\n",
    "\n",
    "#Here is the actual lambda function for the list\n",
    "numbers_sorted = sorted(numbers, key=lambda x: x)\n",
    "\n",
    "#If you wanted to see the actual sorted list\n",
    "print(numbers_sorted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Apple', 'organic'), ('Carrot', 'organic'), ('Tomato', 'organic')]\n"
     ]
    }
   ],
   "source": [
    "#List of foods (I'm choosing organic vs inorganic)\n",
    "foods = [(\"Apple\", \"organic\"), (\"Banana\", \"inorganic\"), (\"Carrot\", \"organic\"), (\"Lettuce\", \"inorganic\"), (\"Tomato\", \"organic\")]\n",
    "\n",
    "#Using the filter() to filter out organic vs inorganic\n",
    "organic_foods = filter(lambda food: food[1] == \"organic\", foods)\n",
    "\n",
    "#Taking what I filtered and printing the list\n",
    "organic_foods_list = list(organic_foods)\n",
    "print(organic_foods_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Apple is red', 'Banana is yellow', 'Carrot is orange', 'Lettuce is green', 'Tomato is red']\n"
     ]
    }
   ],
   "source": [
    "# List of foods with their color\n",
    "foods = [(\"Apple\", \"red\"), \n",
    "         (\"Banana\", \"yellow\"), \n",
    "         (\"Carrot\", \"orange\"), \n",
    "         (\"Lettuce\", \"green\"), \n",
    "         (\"Tomato\", \"red\")]\n",
    "#Now I'll use the map() to describe the food using their color\n",
    "food_descriptions=map(lambda food: f\"{food[0]} is {food[1]}\", foods)\n",
    "\n",
    "#Taking the map and printing the results\n",
    "food_descriptions_list = list(food_descriptions)\n",
    "print(food_descriptions_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28\n"
     ]
    }
   ],
   "source": [
    "#Had to use from functools and use import reduce\n",
    "from functools import reduce\n",
    "\n",
    "#I'll use just integers and show the sum to reduce the group into one value\n",
    "numbers = [1, 2, 3, 4, 5, 6, 7]\n",
    "\n",
    "#This is where the actual reduction takes place\n",
    "result =reduce(lambda x, y: x + y, numbers)\n",
    "\n",
    "#Printed result\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index: 0, Fruit: Apple\n",
      "Index: 1, Fruit: Banana\n",
      "Index: 2, Fruit: Cherry\n",
      "Index: 3, Fruit: Date\n"
     ]
    }
   ],
   "source": [
    "#For this I'll use the list of fruits again\n",
    "fruits = ['Apple', 'Banana', 'Cherry', 'Date']\n",
    "\n",
    "#Without almbda, I'll use enumerate to print the index and fruit\n",
    "for index, fruit in enumerate(fruits):\n",
    "    print(f\"Index: {index}, Fruit: {fruit}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Calico: 4.5 kg\n",
      "Tuxedo: 3.0 kg\n",
      "Orange: 5.0 kg\n"
     ]
    }
   ],
   "source": [
    "#I'll use cat types, and cat weights \n",
    "cat_types = ['Calico', 'Tuxedo', 'Tabby', 'Bombay', 'Orange']\n",
    "weights = [4.5, 3.0, 8.0, 6.5, 5.0]\n",
    "\n",
    "#Using zip and lambda, I can filter out eights greater than 5 kg\n",
    "filtered_types = filter(lambda x: x[1] <= 5, zip(cat_types, weights))\n",
    "\n",
    "#The printed results\n",
    "for types, weight in filtered_types:\n",
    "    print(f\"{types}: {weight} kg\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
