"""
Bonus pay

"""
import csv

def bonus_slots(slot_file = 'slots.txt', type_field = 'Type', range_field = 'Range', bonus_field = 'Bonus'):
    try:
        with open(slot_file, 'r') as f_in:
            bonuses = {}
            bonus_range = {}
            linereader = csv.DictReader(f_in)
            for row in linereader:
                # print(row)
                bonuses[row[type_field]] = int(row[bonus_field])
                bonus_range[row[type_field]] = [
                    int(row[range_field].split('-')[0]), 
                    int(row[range_field].split('-')[1])]
        return bonuses, bonus_range
    except Exception as e:
        print(f'problems with slot file: {e}')
        return None, None

def find_score(scores_file, id_column, score_col, id):
    try:
        with open(scores_file, 'r') as f_in:
            d_reader = csv.DictReader(f_in)
            # header = d_reader.fieldnames
            for line in d_reader:
                if line[id_column] == str(id):
                    # print(f'Score: {line[score_col]} for id = {id}')
                    return int(line[score_col])
            else:
                return None
    except Exception as e:
        print(f'problems with scores file: {e}')
        return None

def find_bonus(score, slot_file = 'slots.txt', type_field = 'Type', range_field = 'Range', bonus_field = 'Bonus'):
    bonuses, ranges = bonus_slots(slot_file, type_field, range_field, bonus_field)
    for key, value in ranges.items():
        if score in range(value[0], value[1]+1):
            return bonuses[key], key
    
if __name__ == '__main__':
    # paramenters for names file
    names = 'names2.txt'
    id_column_names = 'ID'
    names_with_bonus = 'names1_bonus.txt'
    # paramters for scores file
    scores_file = 'scores1.txt'
    id_column_scores = 'ID'
    scores_col = 'Score'
    # main loop: reads each line of names
    # search for id in scores
    # if found, compose the newline with all fields in names
    # plus the score
    bonus_field_name = 'Bonus'
    # then writes the newline to the names_with_bonus file
    with_score = 0
    try:
        with \
            open(names, 'r') as f_in, \
            open(names_with_bonus, 'w', newline='') as f_out:
            d_reader = csv.DictReader(f_in)
            headers = d_reader.fieldnames
            headers.append(bonus_field_name)
            d_writer = csv.DictWriter(f_out, fieldnames=headers)
            d_writer.writeheader()
            bonus_paid = {}
            total_bonus = 0
            for line in d_reader:
                score = find_score(
                    scores_file,
                    id_column_scores, 
                    scores_col,
                    line[id_column_names])
                if score:
                    bonus, bonus_type = find_bonus(score)
                    print(score, bonus_type, bonus)
                    with_score += 1
                    line[bonus_field_name]=bonus
                    d_writer.writerow(line)
                    total_bonus += bonus
                    if bonus_paid.get(bonus_type):
                        bonus_paid[bonus_type] += bonus
                    else:
                        bonus_paid[bonus_type] = bonus
            print(bonus_paid, total_bonus)
            print(with_score)
    except Exception as e:
        print(e)
