

# קודם אני אסביר בעברית מה התכוונתי לעשות - בסוף כתבתי הערות באנגלית וכמובן דוגמה באנגלית:
#1. עלינו לקבוע את סכום השכירות הכולל שיחולק בין הקבוצה.
# ניתן לעשות זאת בכך שנסכום את דמי השכירות שכל אחד מהאנשים בקבוצה משלם.
# 2. נחשב את סכום השכירות המינימלי שכל אחד בקבוצה מוכן לשלם.
# אפשר לחשב את זה דרך זה שנניח שהסכום המינימלי שאדם מהקבוצה משלם כולם היו מוכנים לשלם כי הם משלמים יותר מהסכום הזה כרגע
# 3. הגדרנו את סכום השכירות שמשולם על ידי כולם ואת סכום ההשכירות המינימלי.
# 4. נשתמש בנוסחה :   egalitarian_rent = total_rent / number_of_people
# כדי לחשב חלוקה שיוויונית של חדרים ושכר הדירה
# בנוסחה: total_rent הוא הסכום הכולל של שכר הדירה שיש לחלק בין הקבוצה,
# ומספר_of_people הוא מספר האנשים בקבוצה.
#5. נוכל לחלק את שכר הדירה השוויוני בין הקבוצה על ידי הקצאת מחיר חדש שכל אחד בקבוצה ישלם וכך נקבל שכר דירה שוויוני.
# זה יבטיח שכולם בקבוצה ישלמו את אותו סכום שכר דירה,
# וההפרשים בין כל אחד בקבוצה (ההפרשים המקורים שהיו כאשר כל אחד שילם סכום אחר)
# יחסית קטן עד אפסילון, כאן כולם ישלמו את אותו השכר דירה ולכן זה בהכרח שווה.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~;
# q5:
# Define a function to calculate the egalitarian division of rooms and rent
def egalitarian_division(rents):
  # Calculate the total rent
  total_rent = sum(rents)

  # Calculate the minimum rent amount
  # represents the lowest amount of rent that any person in the group is willing to pay
  min_rent = min(rents)
  # Calculate the egalitarian rent
  egalitarian_rent = total_rent / len(rents)

  # helps us ensure that the egalitarian rent we calculate
  # is not lower than the minimum rent amount, which would not be fair
  # to the people in the group who are willing to pay more
  # also helps us avoid any potential conflicts or disagreements that may arise if the egalitarian rent is too low.
  if min_rent>egalitarian_rent : return -1

  # Return the egalitarian rent
  return egalitarian_rent
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~;

# main fnction:
# Define a list of rents to be divided among a group of people
rents = [500, 600, 700, 800, 900]
# Calculate the egalitarian division of rooms and rent
egalitarian_rent = egalitarian_division(rents)
# Print the egalitarian rent
print(egalitarian_rent)
# Define a list of rents to be divided among a group of people
rents = [500, 500, 10, 8, 900]
# Calculate the egalitarian division of rooms and rent
egalitarian_rent = egalitarian_division(rents)
# Print the egalitarian rent
print(egalitarian_rent)

#In this example, the total rent to be divided among the group is
# 500 + 600 + 700 + 800 + 900 = 3500. The minimum rent amount is 500,
# and the egalitarian rent is 3500 / 5 = 700. This means that each person
# in the group will pay 700 in rent, and the utility is the lowest of any
# player is as high as possible.