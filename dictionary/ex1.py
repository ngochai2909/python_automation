def email_list(domains):
    emails = []
    # Iterate through the dictionary
    for domain, users in domains.items():
        # Iterate through the list of users for each domain
        for user in users:
            # Construct the email and add to the list
            emails.append(f"{user}@{domain}")
    return emails

# Example usage
print(email_list({
    "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
    "yahoo.com": ["barbara.gordon", "jean.grey"],
    "hotmail.com": ["bruce.wayne"]
}))