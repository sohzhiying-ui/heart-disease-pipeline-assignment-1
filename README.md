# heart-disease-pipeline-assignment-1
CI/CD Pipeline with GitHub Actions for Duplicate Removal
Minor edit to trigger workflow
## Running the Pipeline

To remove duplicates locally:
```bash
python scripts/remove_duplicates.py
```markdown
## Running Tests

To run tests locally, make sure Python can find the `scripts` folder.  
Use this command:

```bash
PYTHONPATH=. pytest tests/
