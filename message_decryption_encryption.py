alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''a''b''c''d''e''f''g''h''i''j''k''l''m''n''o''p''q''r''s''t''v''w''x''y''z']
def ceaser(start_text,shift_amount,cipher_direction):
    end_text""
    if cipher_direction == "decode":
        shift_amount * = -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"here's the {cipher_direction}d result   : {end_text}")
    
should_end = False
while not should_end:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("type your message\n").lower()
    shift = int(input("type the shift number\n"))
    shift = shift + 5
    ceaser(start_text = text, shift_amount = shift, cipher_directionn = direction)
    restart = input("type 'yes' if you want to go again,  else type 'no'.\n")
    if restart =="no":
        should_end = True
        print("bye")
