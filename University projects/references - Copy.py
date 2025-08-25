# A program to capitalize the references
# Luyanda Ntombela
# 03 April 2025

# references.py

reference = input("Enter the reference:\n")

# Step 1: Find where the title starts — it comes after ") "
year_end_index = reference.find(") ")
if year_end_index == -1:
    print("Invalid reference format.")
else:
    # Step 2: Break the reference into 3 parts
    # Authors: from start to the space after year
    # Title: from after year to the first comma after the title
    # Rest: everything after the comma

    author_part = reference[:year_end_index + 2]  # includes ") "
    rest_part_start = reference.find(",", year_end_index)
    title_part = reference[year_end_index + 2:rest_part_start]
    rest_part = reference[rest_part_start:]

    # Step 3: Format author names — title case
    formatted_authors = ''
    idx_open_paren = author_part.find('(')
    author_names = author_part[:idx_open_paren].strip()
    year_section = author_part[idx_open_paren:]  # includes (year)

    formatted_authors = author_names.title() + " " + year_section

    # Step 4: Format title — only first letter capitalized
    title_part = title_part.strip()
    if len(title_part) > 0:
        formatted_title = title_part[0].upper() + title_part[1:].lower()
    else:
        formatted_title = ''

    # Step 5: Combine all parts
    formatted_reference = formatted_authors + formatted_title + rest_part

    print("Reformatted reference:")
    print(formatted_reference)


        