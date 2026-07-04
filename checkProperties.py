import os

def extract_css_properties(file_path):
    # Use a set to automatically enforce distinct/unique values
    unique_properties = set()
    
    # Check if file exists before opening
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            
            # Skip empty lines, closing brackets, or comment lines
            if not line or line.startswith('}') or line.startswith('/*') or line.startswith('*/'):
                continue
                
            # Only process lines that contain a colon
            if ':' in line:
                # split(..., 1) ensures we only split at the FIRST colon 
                # (protecting pseudo-classes or URLs like background: url(http://...))
                parts = line.split(':', 1)
                
                # Get the property name and clean up extra whitespace
                property_name = parts[0].strip()
                
                # Filter out CSS selectors, media queries, or symbols that aren't properties
                if property_name and not property_name.startswith('@') and not property_name.startswith('.') and property_name not in unique_properties:
                    unique_properties.add(property_name)
                    
    # Convert the set back to a standard list
    return list(unique_properties)

# Example usage:
# Replace 'styles.css' with your actual file path
css_file = 'styles.css'
distinct_properties = extract_css_properties(css_file)

print(f"Found {len(distinct_properties)} distinct CSS properties:")
print(distinct_properties)