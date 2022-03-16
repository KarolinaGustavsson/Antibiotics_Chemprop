#!/usr/bin/env python3

'''
Usage: ./sdf_to_csv.py <input-filename> <output-filename>

Defaults to `input.sdf` as input and `output.csv` as output,
if no filenames are provided. Exits with error with no input
file was found.
'''


def extract_items(filename):
    with open(filename) as f:
        lines = f.readlines()

    list_smiles = []
    list_coconut_id = []
    items_count = 0

    for n, l in enumerate(lines):

        if '<coconut_id>' in l.strip():
            coconut_id = lines[n+1].strip()
            list_coconut_id.append(coconut_id)

        elif '<SMILES>' in l.strip():
            smiles = lines[n+1].strip()
            list_smiles.append(smiles)

        elif '$$$$' in l.strip():
            items_count += 1

    # Make sure all item counts are in agreement
    assert len(list_smiles) == len(list_coconut_id), 'SMILES and Coconut ID count mismatch.'
    assert len(list_smiles) == items_count, 'SMILES and items count mismatch.'

    return list(zip(list_smiles, list_coconut_id))


def save_to_csv(records, filename):
    lines = []

    # Add headers
    headers = ['smiles', 'ID']
    lines.append(','.join(headers) + '\n')

    # Add records
    for record in records:
        lines.append(','.join(record) + '\n')

    # Add .csv to filename if needed
    if not filename.lower().endswith('.csv'):
        filename = filename + '.csv'

    with open(filename, 'w') as f:
        f.writelines(lines)

    print(f'\n{len(records)} records were successfully written to {filename}')


def save(items, filetype, filename):
    if filetype == 'csv':
        save_to_csv(items, filename)
    else:
        raise SystemExit(f'Error: Output filetype \'{filetype}\' not supported.')


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        print(__doc__.strip())
        raise SystemExit

    if len(sys.argv) == 2:
        input_filename = sys.argv[1]
        output_filename = 'output.csv'
    elif len(sys.argv) == 3:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    else:
        input_filename = 'input.sdf'
        output_filename = 'output.csv'

        print(__doc__.strip())

    compounds = extract_items(input_filename)
    save(compounds, 'csv', output_filename)
