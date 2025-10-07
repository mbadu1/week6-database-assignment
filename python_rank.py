import pandas as pd
import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('university_rankings.db')

print("=" * 60)
print("University Rankings Database Analysis")
print("=" * 60)
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

# 1. INSERT - Add Duke Tech for 2014

print("\n1. INSERT OPERATION - Adding Duke Tech")
print("-" * 60)

# Read the current data
df = pd.read_sql_query("SELECT * FROM university_rankings", conn)

print(f"Records before insert: {len(df)}")

# Create new record
new_university = {
    'institution': 'Duke Tech',
    'country': 'USA',
    'year': 2014,
    'world_rank': 350,
    'score': 60.5
}

# Add to DataFrame
df_new = pd.DataFrame([new_university])
df = pd.concat([df, df_new], ignore_index=True)

# Save back to database
df.to_sql('university_rankings', conn, if_exists='replace', index=False)

print(f"Records after insert: {len(df)}")
print("\nDuke Tech record:")
print(df[df['institution'] == 'Duke Tech'])

# Verify insertion
duke_tech = df[(df['institution'] == 'Duke Tech') & (df['year'] == 2014)]
print(f"\n✓ Successfully inserted {len(duke_tech)} record(s)")


# 2. Count Japan Top 200 (2013)

print("\n\n2. READ OPERATION - Japanese Universities in Top 200 (2013)")
print("-" * 60)

# Read data
df = pd.read_sql_query("SELECT * FROM university_rankings", conn)

# Filter for Japan, 2013, and top 200
japan_top_200 = df[
    (df['country'] == 'Japan') & 
    (df['year'] == 2013) & 
    (df['world_rank'] <= 200)
]

print(f"Count of Japanese universities in top 200 (2013): {len(japan_top_200)}")

print("\nList of universities:")
print(japan_top_200[['institution', 'world_rank', 'score']].sort_values('world_rank'))

print(f"\n✓ Found {len(japan_top_200)} Japanese universities in top 200")

# 3. Update Oxford Score

print("\n\n3. UPDATE OPERATION - Increase Oxford's 2014 Score by 1.2")
print("-" * 60)

# Read data
df = pd.read_sql_query("SELECT * FROM university_rankings", conn)

# Find Oxford in 2014 (before update)
oxford_before = df[
    (df['institution'].str.contains('Oxford', case=False, na=False)) & 
    (df['year'] == 2014)
].copy()

if not oxford_before.empty:
    print("Before update:")
    print(oxford_before[['institution', 'year', 'score']])
    
    old_score = oxford_before['score'].values[0]
    
    # Update the score
    df.loc[
        (df['institution'].str.contains('Oxford', case=False, na=False)) & 
        (df['year'] == 2014),
        'score'
    ] += 1.2
    
    # Save back to database
    df.to_sql('university_rankings', conn, if_exists='replace', index=False)
    
    # Verify update
    oxford_after = df[
        (df['institution'].str.contains('Oxford', case=False, na=False)) & 
        (df['year'] == 2014)
    ]
    
    print("\nAfter update:")
    print(oxford_after[['institution', 'year', 'score']])
    
    new_score = oxford_after['score'].values[0]
    print(f"\n✓ Score changed from {old_score:.2f} to {new_score:.2f} (+1.2)")
else:
    print("⚠ Oxford not found in 2014 data")

#  Remove Low Scores (2015)

print("\n\n4. DELETE OPERATION - Remove universities with score < 45 (2015)")
print("-" * 60)

# Read data
df = pd.read_sql_query("SELECT * FROM university_rankings", conn)

# Count records to delete
to_delete = df[(df['year'] == 2015) & (df['score'] < 45)]
count_to_delete = len(to_delete)

print(f"Records to delete: {count_to_delete}")

if count_to_delete > 0:
    print("\nUniversities to be deleted:")
    print(to_delete[['institution', 'country', 'score']].head(10))
    if count_to_delete > 10:
        print(f"... and {count_to_delete - 10} more")
    
    # Store count before deletion
    records_before = len(df[df['year'] == 2015])
    
    # Delete records
    df = df[~((df['year'] == 2015) & (df['score'] < 45))]
    
    # Save back to database
    df.to_sql('university_rankings', conn, if_exists='replace', index=False)
    
    # Verify deletion
    records_after = len(df[df['year'] == 2015])
    
    print(f"\n2015 records before deletion: {records_before}")
    print(f"2015 records after deletion: {records_after}")
    print(f"✓ Successfully deleted {count_to_delete} records")
else:
    print("No records found to delete")

# Close connection
conn.close()
print("\n" + "=" * 60)
print("All operations completed successfully!")
print("=" * 60)