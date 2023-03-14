class Sel_notes:

    notes_num = []
    for n in range(0,17,1):
        notes_num.append(n)
    note_names = ['A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6']

    # notes = {
    # 1: 'A4', 
    # 2: 'A#4', 
    # 3: 'B4', 
    # 4: 'C5', 
    # 5: 'C#5', 
    # 6: 'D5', 
    # 7: 'D#5', 
    # 8: 'E5', 
    # 9: 'F5', 
    # 10: 'F#5', 
    # 11: 'G5', 
    # 12: 'G#5', 
    # 13: 'A5', 
    # 14: 'A#5', 
    # 15: 'B5',
    # 16: 'C6'}

    note_dict = {}

    

    def __init__(self, notes_num, note_names):
        self.notes = notes_num
        self.note_names = note_names

    def make_dict(self):
        for n in range(self.notes_num):
            self.note_dict.values(zip(n, self.note_names))
    
        return print(self.note_dict)
    print(note_dict)

Sel_notes.make_dict