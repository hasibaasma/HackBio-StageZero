# 🧬 Team Lysine Information Script
"""
HackBio Team Script
Author: Hasiba Asma (Team Lysine)
Purpose:
    - Store and display information about each team member and their favorite gene.
    - Demonstrates clean, modular, and well-documented Python code.
    - Example of data handling for bioinformatics-inspired metadata.
"""


# Function to validate a DNA sequence
def validate_dna(sequence):
    valid_bases = ["A", "T", "G", "C"]
    for base in sequence:
        if base not in valid_bases:
            return False
    return True

# Function to display information for one member
def display_member_info(member):
    print("=" * 60)
    print("Name:", member["Name"])
    print("Slack Username:", member["Slack Username"])
    print("Country:", member["Country"])
    print("Hobby:", member["Hobby"])
    print("Affiliation:", member["Affiliation"])
    print("Favorite Gene:", member["Favorite Gene"])
    print("DNA Sequence:", member["DNA Sequence"])
    
    # Validate DNA sequence
    dna_only = member["DNA Sequence"].split("\n")[-1]  # get only the sequence line
    if validate_dna(dna_only):
        print("DNA Validation: ✅ Valid sequence")
    else:
        print("DNA Validation: ❌ Invalid sequence")
    print("=" * 60)
    print()

# Function to display information for all team members
def display_team_info(team):
    print("\n===== TEAM Lysine =====\n")
    for member in team:
        display_member_info(member)

# Main function
def main():
    team = [
        {
            "Name": "Hasiba Asma",
            "Slack Username": "Hasiba Asma",
            "Country": "Pakistan 🇵🇰",
            "Hobby": "Exploring AI with bioinformatics",
            "Affiliation": "Sepal AI",
            "Favorite Gene": "Hox gene (controls body plan and segment identity)",
            "DNA Sequence": ">NM_005522.5 HOXA1 [Homo sapiens]\nATCATTTTTCTTCTCCGGCCCCATGGAGGAAGTGAGAAAGTTGGCACAGTCACGCCGGGCTTCGCAGGAC"
        },
        {
            "Name": "Zakia Salod",
            "Slack Username": "Zakia Salod",
            "Country": "South Africa 🇿🇦",
            "Hobby": "Art",
            "Affiliation": "University of KwaZulu-Natal",
            "Favorite Gene": "CCR5 (HIV co-receptor gene)",
            "DNA Sequence": ">NM_001394783.1 CCR5 [Homo sapiens]\nATGGATTATCAAGTGTCAAGTCCAATCTATGACATCAATTATTATACATCGGAGCCCTGCCAAAAAATCA"
        },
        {
            "Name": "Abane Louis Ashu",
            "Slack Username": "Louis",
            "Country": "Cameroon 🇨🇲",
            "Hobby": "Investing and Trading",
            "Affiliation": "Université Libre de Bruxelles (ULB)",
            "Favorite Gene": "GATA6 (key regulator of heart and pancreas development)",
            "DNA Sequence": ">NM_005257.6 GATA6 [Homo sapiens]\nGGACTCGCGCTCGCCCGCTGGCGCCCTCGGCTTCTCTCCGCGCCTGGGAGCACCCTCCGCCGCGGCCGTT"
        },
        {
            "Name": "Aaronie Jersha Jenyfred",
            "Slack Username": "Jersha Fernando",
            "Country": "USA 🇺🇸",
            "Hobby": "Bookreading",
            "Affiliation": "Northeastern University",
            "Favorite Gene": "KRAS (central in cell signaling and cancer biology)",
            "DNA Sequence": ">NC_000001.11 KRAS [Homo sapiens]\nGGGGCCGGAAGTGCCGCTCCTTGGTGGGGGCTGTTCATGGCGGTTCCGGGGTCTCCAACATTTTTCCCGG"
        },
        {
            "Name": "Poornavaishnavi Chekuri",
            "Slack Username": "Vaishnavi",
            "Country": "USA 🇺🇸",
            "Hobby": "Knowledge hunting",
            "Affiliation": "University of Houston-Clear Lake",
            "Favorite Gene": "EGFR (cell growth receptor gene)",
            "DNA Sequence": ">NM_057411.4 EGFR [Drosophila melanogaster]\nAGTCTCGAATACAACTTGTTGCTGCGCGGACGCGAATCGCTCAGTACGGAC"
        }
    ]

    display_team_info(team)

# Run the main program
main()
