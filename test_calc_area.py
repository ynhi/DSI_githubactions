
def test_calc_area_square():
    from calc_area import calc_area_square

    input_number = 2
    output_number = calc_area_square(input_number)
    assert output_number == 4

############################################
# more complicated test below:

# def test_calc_area_square():
#     from calc_area import calc_area_square

#     input_numbers = [0, 1, 4, 100]
#     output_numbers = [0, 1, 16, 10000]
    
#     # option 1
#     for input, output in zip(input_numbers, output_numbers):
#         assert calc_area_square(input) == output
    

#     # option 2
#     for i in range(len(input_numbers)):
#         this_input = input_numbers[i]
#         this_exp_out = output_numbers[i]

#     assert calc_area_square(this_input) == this_exp_out