# 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".

task_string = 'mdnvllабвllllllsfkvsm,sабвsssldklsdsdfs'
print(f'строка условной задачи = {task_string}')

string = 'абв'

answer = "".join(task_string.split(string))  ##Удалит стринг из списка, если в первые кавычки вписать ттекст, то он его вставил

print(f'ответ = {answer}')





