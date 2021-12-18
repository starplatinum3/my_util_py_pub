
def java_code_to_sql(java_code_str):
 
    lines=java_code_str.split("\n")

    for line in lines:
        line=line.replace('" +','')
        line=line.replace('"','')
        print(line)


java_code_str='''
    "select\n" +
                "    user_name,\n" +
                "    sum(exercise_count) ex_cnt_sum,\n" +
                "    user_phone\n" +
                "\n" +
                "from tbl_record,\n" +
                "     tbl_user\n" +
                "where tbl_record.user_id = tbl_user.id\n" +
                "  and tbl_record.delete_flag = 0\n" +
                "  and exercise_id = 0\n" +
                "  and user_phone is not null\n" +
                "  and user_phone <> ''\n" +
                "  and tbl_user.delete_flag=0\n" +
                "  and year(now()) = year(tbl_record.create_time)\n" +
                "  and month(now()) = month(tbl_record.create_time)\n" +
                "group by user_phone,user_name";
    '''

java_code_to_sql(java_code_str)