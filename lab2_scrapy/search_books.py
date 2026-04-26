import json
import sys

def load_books(filename='books.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def search_by_title(books, query):
    query = query.lower()
    return [b for b in books if query in b.get('title', '').lower()]

def filter_by_price(books, max_price_str):
    try:
        max_price = float(max_price_str)
    except ValueError:
        print('Invalid price value')
        return []
    results = []
    for b in books:
        price_raw = b.get('price', '£0').replace('Â', '').replace('£', '').strip()
        try:
            price = float(price_raw)
        except ValueError:
            continue
        if price <= max_price:
            results.append(b)
    return results

def filter_by_rating(books, rating):
    rating = rating.strip().capitalize()
    return [b for b in books if b.get('rating', '').strip().capitalize() == rating]

def print_books(books):
    if not books:
        print("No books found.")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. {b.get('title', 'N/A')} | Price: {b.get('price')} | "
              f"Stock: {b.get('stock')} | Rating: {b.get('rating')} | "
              f"Category: {b.get('category')} | URL: {b.get('url')}")
    print(f"Total: {len(books)} books.\n")

def menu():
    print("\n=== Book Search Interface ===")
    print("1. Search by title")
    print("2. Filter by maximum price")
    print("3. Filter by rating")
    print("4. Show all books")
    print("5. Exit")
    return input("Enter choice (1-5): ").strip()

def main():
    try:
        books = load_books('books.json')
    except FileNotFoundError:
        print("books.json not found. Run the scraper first.")
        sys.exit(1)

    while True:
        choice = menu()
        if choice == '1':
            q = input("Enter title (or part): ")
            print_books(search_by_title(books, q))
        elif choice == '2':
            p = input("Enter maximum price (number): ")
            print_books(filter_by_price(books, p))
        elif choice == '3':
            r = input("Enter rating (One, Two, Three, Four, Five): ")
            print_books(filter_by_rating(books, r))
        elif choice == '4':
            print_books(books)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()