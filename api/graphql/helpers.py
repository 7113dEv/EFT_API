import re

# def load_query(file_path: str, query_name: str) -> str:
#     try:
#         file_content = None

#         with open(file_path, 'r') as f:
#             file_content = f.read()

        
#         print(f"Loaded query file content:\n{file_content[:10]}...") 

#         query_name_pattern = rf'query\s+{query_name}\b[^\{{]*\{{[^}}]*\}}'
#         name_match = re.search(pattern=query_name_pattern, string=file_content, flags=re.DOTALL)

#         if not name_match:
#             raise ValueError(f"Query '{query_name}' not found in {file_path}")
        
#         return name_match.group(0)
        
#     except Exception as e:
#         print(f"Exception occurred while loading query. Error: {e} @ {e.__traceback__.tb_lineno}.")
        
def load_query(file_path: str, query_name: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        # Regex pattern to extract the named query block
        pattern = rf'query\s+{query_name}\s*\{{(?:[^{{}}]*|\{{(?:[^{{}}]*|\{{[^{{}}]*\}})*\}})*\}}'
        match = re.search(pattern, file_content, re.DOTALL)

        if not match:
            raise ValueError(f"Query '{query_name}' not found in {file_path}")

        return match.group(0)

    except Exception as e:
        print(f"Exception in load_query: {e} (line {e.__traceback__.tb_lineno})")
        raise

