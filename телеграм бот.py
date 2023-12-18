import telebot
from telebot import types
# Создаем экземпляр бота с указанием токена
bot = telebot.TeleBot('6861874914:AAHUavD6o6493f7jCj78fh8AVw-P-_HqfKw')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Отправляем приветственное сообщение
    bot.send_message(message.chat.id, 'Добрый день! Я робот-помощник Юрий Легаев.', reply_markup=types.ReplyKeyboardRemove())
    get_main_menu(message)


# Функция для получения главного меню
def get_main_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Получить консультацию юриста', callback_data='1')
    b2 = types.InlineKeyboardButton('Локальные нормативные акты Общества', callback_data='2')
    b3 = types.InlineKeyboardButton('Договорная работа', callback_data='3')
    b4 = types.InlineKeyboardButton('Закупки', callback_data='4')
    b5 = types.InlineKeyboardButton('Информация для работников', callback_data='5')
    b6 = types.InlineKeyboardButton('Служба качества', callback_data='6')
    b7 = types.InlineKeyboardButton('Страхование', callback_data='7')
    b8 = types.InlineKeyboardButton('Учредительные документы', callback_data='8')
    b9 = types.InlineKeyboardButton('Калькуляторы', callback_data='9')
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    bot.send_message(message.chat.id, 'Введите Ваш запрос с клавиатуры или выберите интересующий Вас раздел:', reply_markup=markup)

#
# Функция для полючения меню "Получить консультацию юриста"
def get_legal_advice_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Договор', callback_data='legal_advice_1')
    b2 = types.InlineKeyboardButton('Доверенность', callback_data='legal_advice_2')
    b3 = types.InlineKeyboardButton('Суд', callback_data='legal_advice_3')
    b4 = types.InlineKeyboardButton('Претензия', callback_data='legal_advice_4')
    b5 = types.InlineKeyboardButton('Иное', callback_data='legal_advice_5')
    markup.add(b1, b2, b3, b4, b5)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


# Функция для получения меню "Локальные нормативные акты общества"
def get_local_regulations_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Безопасность', callback_data='local_regulations_1')
    b2 = types.InlineKeyboardButton('Делопроизводство', callback_data='local_regulations_2')
    b3 = types.InlineKeyboardButton('Договорная работа', callback_data='local_regulations_3')
    b4 = types.InlineKeyboardButton('Закупки', callback_data='local_regulations_4')
    b5 = types.InlineKeyboardButton('Коммерческая и операционная работа', callback_data='local_regulations_5')
    b6 = types.InlineKeyboardButton('Трудовые отношения', callback_data='local_regulations_6')
    b7 = types.InlineKeyboardButton('Охрана труда', callback_data='local_regulations_7')
    b8 = types.InlineKeyboardButton('Коллективный договор', callback_data='local_regulations_8')
    b9 = types.InlineKeyboardButton('Финансы и бух. учёт', callback_data='local_regulations_9')
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


# Функция для получения меню "Договорная работа"
def get_contract_work_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Оговорки', callback_data='contract_work_1')
    b2 = types.InlineKeyboardButton('Полезное(схемы, рекомендации, запрашиваемые у контрагента)', callback_data='contract_work_2')
    b3 = types.InlineKeyboardButton('Регламентирующие документы', callback_data='contract_work_3')
    b4 = types.InlineKeyboardButton('Рекомендованные формы договоров', callback_data='contract_work_4')
    b5 = types.InlineKeyboardButton('Типовые формы договоров, соглашений', callback_data='contract_work_5')
    markup.add(b1, b2, b3, b4, b5)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


# Функция для получения меню "Оговорки"
def get_reservations_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Антикоррупционная оговорка', callback_data='reservations_1')
    b2 = types.InlineKeyboardButton('Налоговая оговорка', callback_data='reservations_2')
    b3 = types.InlineKeyboardButton('Оговорка о конфиденциальности', callback_data='reservations_3')
    b4 = types.InlineKeyboardButton('Санкционная оговорка_Иран', callback_data='reservations_4')
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


# Функция для получения меню "Полезное"
def get_useful_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Документы, запрашиваемые от контрагентов', callback_data='useful_1')
    b2 = types.InlineKeyboardButton('Инструкция по договорной работе', callback_data='useful_2')
    b3 = types.InlineKeyboardButton('Памятка_Договорная работа с иностранными контрагентами', callback_data='useful_3')
    b4 = types.InlineKeyboardButton('Прошито, пронумеровано', callback_data='useful_4')
    b5 = types.InlineKeyboardButton('Реквизиты РЖДЛ', callback_data='useful_5')
    b6 = types.InlineKeyboardButton('Типичные разногласия к договорам', callback_data='useful_6')
    b7 = types.InlineKeyboardButton('Чек-лист по договорной работе', callback_data='useful_7')
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


# Функция для получения меню "Регламентирующие документы"
def get_regulatory_documents_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Положение о договорной работе', callback_data='regulatory_documents_1')
    markup.add(b1)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Рекомендованные формы договоров"
def get_recommended_forms_of_contracts_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Агентский договор для работников ОАО РЖД (ЦФТО)', callback_data='recommended_forms_of_contracts_1')
    b2 = types.InlineKeyboardButton('Договор аренды локомотива_расходный', callback_data='recommended_forms_of_contracts_2')
    b3 = types.InlineKeyboardButton('Договор на автоперевозки_расходный', callback_data='recommended_forms_of_contracts_3')
    b4 = types.InlineKeyboardButton('Договор оказания маневровых услыг (доходный)', callback_data='recommended_forms_of_contracts_4')
    b5 = types.InlineKeyboardButton('Договор оказания услуг по погрузке-разгрузке грузов_доходный', callback_data='recommended_forms_of_contracts_5')
    b6 = types.InlineKeyboardButton('Договор поставки сырья с транспортными услугами (доходный)', callback_data='recommended_forms_of_contracts_6')
    b7 = types.InlineKeyboardButton('Договор поставки_АХО_расходный', callback_data='recommended_forms_of_contracts_7')
    b8 = types.InlineKeyboardButton('Договор ТЭО на платежно-финансовые услуги (доходный)', callback_data='recommended_forms_of_contracts_8')
    b9 = types.InlineKeyboardButton('Доп. соглашение изменение пункта в договоре (шаблон)', callback_data='recommended_forms_of_contracts_9')
    b10 = types.InlineKeyboardButton('Доп. соглашение о продлении срока действия договора', callback_data='recommended_forms_of_contracts_10')
    b11 = types.InlineKeyboardButton('Доп. соглашение_предоставление отсрочки_к доходному договору', callback_data='recommended_forms_of_contracts_11')
    b12 = types.InlineKeyboardButton('Доп. соглашение_расторжение договора', callback_data='recommended_forms_of_contracts_12')
    b13 = types.InlineKeyboardButton('Сетевые соглашения (ДОХ, РАСХ)', callback_data='recommended_forms_of_contracts_13')
    b14 = types.InlineKeyboardButton('Соглашение о сотрудничестве', callback_data='recommended_forms_of_contracts_14')
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Типовые формы договоров, соглашений"
def get_standard_forms_of_contract_agreements_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Агентский договор_МПГ', callback_data='standard_forms_of_contract_agreements_1')
    b2 = types.InlineKeyboardButton('Договор на оказание услуг таможенного представителя_доходный', callback_data='standard_forms_of_contract_agreements_2')
    b3 = types.InlineKeyboardButton('Договор на перевозки грузов автомобильным транспортом_расходный', callback_data='standard_forms_of_contract_agreements_3')
    b4 = types.InlineKeyboardButton('Договор об оказании услуг по организации диспетчерского сопровождения подвижного состава (грузовой шаттл)_доходный', callback_data='standard_forms_of_contract_agreements_4')
    b5 = types.InlineKeyboardButton('Договор транспортной экспедиции (МПГ)_доходный', callback_data='standard_forms_of_contract_agreements_5')
    b6 = types.InlineKeyboardButton('Договор транспортной экспедиции _доходный (с резидентом РФ)', callback_data='standard_forms_of_contract_agreements_6')
    b7 = types.InlineKeyboardButton('Договор транспортной экспедиции_доходный (с НЕрезидентом РФ)  РУС_АНГЛ // РУС_КИТ //  РУС_АНГЛ_КИТ', callback_data='standard_forms_of_contract_agreements_7')
    b8 = types.InlineKeyboardButton('Договор транспортной экспедиции_доходный (с НЕрезидентом РФ)_одноязычный', callback_data='standard_forms_of_contract_agreements_8')
    b9 = types.InlineKeyboardButton('Договор_предоставление ПС_расходный', callback_data='standard_forms_of_contract_agreements_9')
    b10 = types.InlineKeyboardButton('Договор_ТЭО_расходный', callback_data='standard_forms_of_contract_agreements_10')
    b11 = types.InlineKeyboardButton('Договор_ТЭО_транспортеры_с услугами ТП_доходный', callback_data='standard_forms_of_contract_agreements_11')
    b12 = types.InlineKeyboardButton('Доп. соглашение к договору ТЭО_на таможенные услуги', callback_data='standard_forms_of_contract_agreements_12')
    b13 = types.InlineKeyboardButton('ДС_об особенностях оказания услуг в вагонах-транспортерах', callback_data='standard_forms_of_contract_agreements_13')
    b14 = types.InlineKeyboardButton('Соглашение о конфиденциальности и неразглашении информации', callback_data='standard_forms_of_contract_agreements_14')
    b15 = types.InlineKeyboardButton('Соглашение об отсрочке', callback_data='standard_forms_of_contract_agreements_15')
    b16 = types.InlineKeyboardButton('Соглашение об электронном документообороте', callback_data='standard_forms_of_contract_agreements_16')
    b17 = types.InlineKeyboardButton('Типовой ДТЭ _Агроэкспресс_оферта', callback_data='standard_forms_of_contract_agreements_17')
    b18 = types.InlineKeyboardButton('Типовой ДТЭ_Оферта и правила оказания услуг', callback_data='standard_forms_of_contract_agreements_18')
    b19 = types.InlineKeyboardButton('Типовой ТЭО расходный с нерезидентом РУС // РУС_АНГЛ // РУС_КИТ', callback_data='standard_forms_of_contract_agreements_19')
    b20 = types.InlineKeyboardButton('Типовой ТЭО с таможенными услугами доходный с резидентом', callback_data='standard_forms_of_contract_agreements_20')
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)

#Функция для получения меню "Закупки"
def get_procurement_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Регламентирующие документы', callback_data='procurement_1')
    b2 = types.InlineKeyboardButton('Типовые формы договоров', callback_data='procurement_2')
    markup.add(b1, b2)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)



#Функция для получения меню "Служба качества"
def get_quality_service_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Внешний аудит', callback_data='quality_service_1')
    b2 = types.InlineKeyboardButton('Внутренний аудит', callback_data='quality_service_2')
    b3 = types.InlineKeyboardButton('Изменения', callback_data='quality_service_3')
    b4 = types.InlineKeyboardButton('Несоответствия', callback_data='quality_service_4')
    b5 = types.InlineKeyboardButton('Стандартные операционные процедуры (СОП)', callback_data='quality_service_5')
    b6 = types.InlineKeyboardButton('Цели по качеству', callback_data='quality_service_6')
    markup.add(b1, b2, b3, b4, b5, b6)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)




#Функция для получения меню "Стандартные операционные процедуры(СОП)"
def get_standard_operating_procedures_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Перечень утвержденной докуменации СМК и СЭМ, СОП', callback_data='standard_operating_procedures_1')
    b2 = types.InlineKeyboardButton('СОП-07-Требования к санитарному состоянию оборудования при транспортировке фарм.продукции версия 01', callback_data='standard_operating_procedures_2')
    b3 = types.InlineKeyboardButton('СОП-08-Требования по санитарным нормам и правилам для персонала версия 01', callback_data='standard_operating_procedures_3')
    b4 = types.InlineKeyboardButton('СОП-10-Порядок работы с системой сигнализации, оповещения и слежения', callback_data='standard_operating_procedures_4')
    b5 = types.InlineKeyboardButton('СОП-11-Порядок предоставления отчетности отделом диспетчеризации версия 01', callback_data='standard_operating_procedures_5')
    b6 = types.InlineKeyboardButton('СОП-13-Требования к поверке средств измерений  версия 01', callback_data='standard_operating_procedures_6')
    b7 = types.InlineKeyboardButton('СОП-16-Требования к процессу транспортировке фармацевтической продукции версия 01', callback_data='standard_operating_procedures_7')
    b8 = types.InlineKeyboardButton('СОП-17-Требования к системе экологического менеджмента версия 01', callback_data='standard_operating_procedures_8')
    b9 = types.InlineKeyboardButton('СОП-18-Правила ведения документированной информации версия 01', callback_data='standard_operating_procedures_9')
    b10 = types.InlineKeyboardButton('СОП-20-Порядок проведения анализа видов и последствий рисков версия 01', callback_data='standard_operating_procedures_10')
    b11 = types.InlineKeyboardButton('СОП-21-Минимизация рисков контаминации ЛС при перевозке версия 01', callback_data='standard_operating_procedures_11')
    b12 = types.InlineKeyboardButton('СОП-22-Порядок погрузки в реф.контейнеры АО «РЖД Логистика»', callback_data='standard_operating_procedures_12')
    #b13 = types.InlineKeyboardButton('СОП-22-Порядок погрузки в реф.контейнеры АО «РЖД Логистика» версия 02', callback_data='standard_operating_procedures_13')
    b13 = types.InlineKeyboardButton('СОП-23-Порядок подготовки фарм. продукции к погрузке версия 01', callback_data='standard_operating_procedures_13')
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Порядок погрузки в реф.контейнеры АО «РЖД Логистика» "
def get_loading_procedure_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Версия 01', callback_data='loading_procedure_1')
    b2 = types.InlineKeyboardButton('Версия 02', callback_data='loading_procedure_2')
    markup.add(b1, b2)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Страхование"
def get_insurance_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Корпоративная концепция страховой защиты компании Холдинга "РЖД"', callback_data='local_insurance_1')
    b2 = types.InlineKeyboardButton('Страхование грузов', callback_data='local_insurance_2')
    b3 = types.InlineKeyboardButton('Страхование ответственности_РЖДЛ', callback_data='local_insurance_3')
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Учредительные документы"
def get_constituent_documents_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Аффилированные лица', callback_data='constituent_documents_1')
    b2 = types.InlineKeyboardButton('Бенефициары', callback_data='constituent_documents_2')
    b3 = types.InlineKeyboardButton('Бухгалтерская отчетность', callback_data='constituent_documents_3')
    b4 = types.InlineKeyboardButton('Внутренние документы, учрежденнные СД', callback_data='constituent_documents_4')
    b5 = types.InlineKeyboardButton('Выписка из ЕГРЮЛ', callback_data='constituent_documents_5')
    b6 = types.InlineKeyboardButton('ДЗО', callback_data='constituent_documents_6')
    b7 = types.InlineKeyboardButton('Документы об учреждении', callback_data='constituent_documents_7')
    b8 = types.InlineKeyboardButton('Ежеквартальные отчеты ГД', callback_data='constituent_documents_8')
    b9 = types.InlineKeyboardButton('Лицензии, сертификаты, разрешения', callback_data='constituent_documents_9')
    b10 = types.InlineKeyboardButton('ОАО РЖД', callback_data='constituent_documents_10')
    b11 = types.InlineKeyboardButton('Полномочия генерального директора', callback_data='constituent_documents_11')
    b12 = types.InlineKeyboardButton('Санкции', callback_data='constituent_documents_12')
    b13 = types.InlineKeyboardButton('Свидетельства о регистрации', callback_data='constituent_documents_13')
    b14 = types.InlineKeyboardButton('Совет директоров', callback_data='constituent_documents_14')
    b15 = types.InlineKeyboardButton('Комитеты', callback_data='constituent_documents_15')
    b16 = types.InlineKeyboardButton('Список акционеров РЖДЛ', callback_data='constituent_documents_16')
    b17 = types.InlineKeyboardButton('Устав', callback_data='constituent_documents_17')
    b18 = types.InlineKeyboardButton('Филиалы', callback_data='constituent_documents_18')
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Лицензии, сертификаты, разрешения"
def get_licenses_certificates_permissions_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Лицензия_ПРР_опасные грузы', callback_data='licenses_certificates_permissions_1')
    b2 = types.InlineKeyboardButton('Свидетельство СРО', callback_data='licenses_certificates_permissions_2')
    b3 = types.InlineKeyboardButton('Таможенная лицензия', callback_data='licenses_certificates_permissions_3')
    b4 = types.InlineKeyboardButton('Лицензия_гостайна', callback_data='licenses_certificates_permissions_4')
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Полномочия генерального директора"
def get_powers_of_the_general_director_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Валентиник В.Б.', callback_data='powers_of_the_general_director_1')
    b2 = types.InlineKeyboardButton('Мурев Д.И._2020', callback_data='powers_of_the_general_director_2')
    b3 = types.InlineKeyboardButton('Мурев Д.И._2021', callback_data='powers_of_the_general_director_3')
    b4 = types.InlineKeyboardButton('Соколов П.В.', callback_data='powers_of_the_general_director_4')
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


#Функция для получения меню "Свидетельства о регистрации"
def get_registration_certificates_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Изменение наименования на АО_2015', callback_data='registration_certificates_1')
    b2 = types.InlineKeyboardButton('Свидетельства о регистрации', callback_data='registration_certificates_2')
    markup.add(b1, b2)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


# Функция для получения меню договора
def get_contract_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Типовые договоры', callback_data='contract_1')
    b2 = types.InlineKeyboardButton('Порядок согласования договора', callback_data='contract_2')
    b3 = types.InlineKeyboardButton('Условие договора', callback_data='contract_3')
    b4 = types.InlineKeyboardButton('Иное', callback_data='contract_4')
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)

# Функция для получения меню доверенность
def get_a_power_of_attorney(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Как оформить доверенность?', callback_data='power_of_attorney_1')
    b2 = types.InlineKeyboardButton('Где найти доверенность?', callback_data='power_of_attorney_2')
    b3 = types.InlineKeyboardButton('Как проверить нотариальную доверенность?', callback_data='power_of_attorney_3')
    b4 = types.InlineKeyboardButton('Действует ли доверенность?', callback_data='power_of_attorney_4')
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)


# Функция для получения меню делопроизводства
def get_document_management_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Внутренний портал корпоративной информации', callback_data='document_management_1')
    b2 = types.InlineKeyboardButton('Инструкция о приеме иностранных делегаций и граждан', callback_data='document_management_2')
    b3 = types.InlineKeyboardButton('Инструкция по делопроизводству', callback_data='document_management_3')
    b4 = types.InlineKeyboardButton('Использование ПЭП во внутреннем документообороте (1С)', callback_data='document_management_4')
    b5 = types.InlineKeyboardButton('ЛК Госуслуги', callback_data='document_management_5')
    b6 = types.InlineKeyboardButton('ЛК участника ВЭД и административное производство по таможне', callback_data='document_management_6')
    markup.add(b1, b2, b3, b4, b5, b6)
    bot.send_message(message.chat.id, 'Выберите интересущий раздел:', reply_markup=markup)
# Функция для получения меню типового договора
def the_standard_form_of_the_contract(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Доходный', callback_data='form_contract_1')
    b2 = types.InlineKeyboardButton('Расходный', callback_data='form_contract_2')
    b3 = types.InlineKeyboardButton('Иное', callback_data='form_contract_3')
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id, 'Если Вам необходима типовая форма договора выберите:', reply_markup=markup)
# Функция для получения доходного раздела
def get_revenue_section(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('С резидентом', callback_data='revenue_section_1')
    b2 = types.InlineKeyboardButton('С нерезидентом', callback_data='revenue_section_2')
    markup.add(b1, b2)
    bot.send_message(message.chat.id, 'Выберите интересующий раздел:', reply_markup=markup)
# Функция для ответа на вопрос Как оформить доверенность?
def how_to_issue_a_power_of_attorney(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Да', callback_data='issue_a_power_of_attorney_1')
    b2 = types.InlineKeyboardButton('Нет', callback_data='issue_a_power_of_attorney_2')
    markup.add(b1, b2)
    bot.send_message(message.chat.id, 'Доверенность нужна для подписания документов по ЭДО?', reply_markup=markup)

#Функция для ответа да на оформление доверенности
def yes_power_of_attorney(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Да', callback_data='power_of_attorney_yes_1')
    b2 = types.InlineKeyboardButton('Нет', callback_data='power_of_attorney_yes_2')
    markup.add(b1, b2)
    bot.send_message(message.chat.id, 'У вас есть ЭЦП?» ', reply_markup=markup)


# Функция для получения калькуляторов
def calculators_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton('Калькулятор гос. пошлины в арбитажный суд', callback_data='calculators_1')
    b2 = types.InlineKeyboardButton('Калькулятор гос. пошлины в суды общей юрисдикции', callback_data='calculators_2')
    b3 = types.InlineKeyboardButton('Калькулятор расчета суммы неустойки', callback_data='calculators_3')
    b4 = types.InlineKeyboardButton('Калькулятор расчета процентов за пользование чужими денежными средствами', callback_data='calculators_4')
    b5 = types.InlineKeyboardButton('Калькулятор расчета индексации присужденных денежных сумм', callback_data='calculators_5')
    markup.add(b1, b2, b3, b4, b5)
    bot.send_message(message.chat.id, 'Выберите нужный Вам калькулятор', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == '1':
        get_legal_advice_menu(call.message)
    elif call.data == 'legal_advice_1':
        get_contract_menu(call.message)
    elif call.data == 'contract_1':
        the_standard_form_of_the_contract(call.message)
    elif call.data == 'form_contract_1':
        get_revenue_section(call.message)
    elif call.data == 'revenue_section_1':
        bot.send_message(call.message.chat.id, 'Типовая форма доходного договора с нерезидентом находится в 1С:Документооборот в разделе Внутренние документы - Портал внутренней корпоративной  информации - Договорная работа - Типовые формы договоров и соглашений')
    elif call.data == 'legal_advice_2':
        get_a_power_of_attorney(call.message)
    elif call.data == 'power_of_attorney_1':
        how_to_issue_a_power_of_attorney(call.message)
    elif call.data == 'issue_a_power_of_attorney_2':
        bot.send_message(call.message.chat.id, 'В 1С :Документооборот оформите заявку на доверенность.  Заявку можно оформить в 1С:Документооброт следующим образом: Создать - Документ внутренний - Заявки  - Заявка на оформление доверенности')
    elif call.data == 'issue_a_power_of_attorney_1':
        yes_power_of_attorney(call.message)
    elif call.data == 'power_of_attorney_yes_1':
        bot.send_message(call.message.chat.id, 'В 1С  оформите «Заявку на выпуск машиночитаемой доверенности (МЧД)». Заявку можно оформить в 1С:Документооброт следующим образом: Создать - Документ внутренний - Заявки  - Заявка на выпуск машиночитаемой  доверенности (МЧД)')
    elif call.data == 'power_of_attorney_yes_2':
        bot.send_message(call.message.chat.id, 'В 1С:Документооборот оформите «Заявка на получение (перевыпуск) ЭЦП».  Заявку можно оформить в 1С:Документооброт следующим образом: Создать - Документ внутренний - Заявки  - Заявка на получение (перевыпуск) ЭЦП. Система автоматически направит заявку на МЧД за Вас')
    elif call.data == '2':
        get_local_regulations_menu(call.message)
    elif call.data == 'local_regulations_2':
        get_document_management_menu(call.message)
    elif call.data == 'document_management_3':
        bot.send_message(call.message.chat.id, 'Актуальная инструкция по делопроизводству расположена в 1С: Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Действующие ЛНА Общества – Делопроизводство')
    elif call.data == '3':
        get_contract_work_menu(call.message)
    elif call.data == 'contract_work_1':
        get_reservations_menu(call.message)
    elif call.data == 'reservations_1':
        bot.send_message(call.message.chat.id, 'Актуальная антикоррупционная оговорка расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Оговорки ')
    elif call.data == 'reservations_2':
        bot.send_message(call.message.chat.id,'Актуальная налоговая оговорка расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Оговорки')
    elif call.data == 'reservations_3':
        bot.send_message(call.message.chat.id, 'Актуальная оговорка о конфиденциальности расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Оговорки')
    elif call.data == 'reservations_4':
        bot.send_message(call.message.chat.id, 'Актуальная санкционная оговорка расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Оговорки')
    elif call.data == 'contract_work_2':
        get_useful_menu(call.message)
    elif call.data == 'useful_1':
        bot.send_message(call.message.chat.id, 'Актуальные документы, запрашиваемые от контаргента  расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Полезное')
    elif call.data == 'useful_2':
        bot.send_message(call.message.chat.id, 'Актуальная инстукция по договорной работе  расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Полезное')
    elif call.data == 'useful_3':
        bot.send_message(call.message.chat.id, 'Актуальная Памятка по договорной работе с иностранными контрагентами расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Полезное')
    elif call.data == 'useful_5':
        bot.send_message(call.message.chat.id, 'Актуальные реквизиты расположены в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Полезное')
    elif call.data == 'useful_6':
        bot.send_message(call.message.chat.id, 'Памятка Актуальная инстукция по договорной работе  расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Полезное')
    elif call.data == 'useful_7':
        bot.send_message(call.message.chat.id, 'Актуальный чек лист по договорной работе  расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Полезное')
    elif call.data == 'contract_work_3':
        get_regulatory_documents_menu(call.message)
    elif call.data == 'regulatory_documents_1':
        bot.send_message(call.message.chat.id, 'Актуальное Положение о договорной работе  расположено в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Регламентирующие документы')
    elif call.data == 'contract_work_4':
        get_recommended_forms_of_contracts_menu(call.message)
    elif call.data == 'recommended_forms_of_contracts_1':
        bot.send_message(call.message.chat.id, 'Актуальный агентский договор для работников ОАО РЖД (ЦФТО) расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_2':
        bot.send_message(call.message.chat.id, 'Актуальный договор аренды локомотива_расходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_3':
        bot.send_message(call.message.chat.id, 'Актуальный договор на автоперевозки_расходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_4':
        bot.send_message(call.message.chat.id, 'Актуальный договор оказания маневровых услуг (доходный) расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_5':
        bot.send_message(call.message.chat.id, 'Актуальный договор оказания услуг  по погрузке-разгрузке_доходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_6':
        bot.send_message(call.message.chat.id, 'Актуальный договор Договор поставки сырья с транспортными услугами (доходный) расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_7':
        bot.send_message(call.message.chat.id, 'Актуальный Договор поставки_АХО_расходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_8':
        bot.send_message(call.message.chat.id, 'Актуальный Договор ТЭО на платежно-финансовые услуги (доходный) расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_9':
        bot.send_message(call.message.chat.id, 'Актуальное Доп соглашение изменение пункта в договоре (шаблон) расположено в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_10':
        bot.send_message(call.message.chat.id, 'Актуальное Доп соглашение о продлении срока действия договора расположено в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_11':
        bot.send_message(call.message.chat.id, 'Актуальное Доп соглашение_предоставление отсрочки_к доходному договору расположено в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_12':
        bot.send_message(call.message.chat.id, 'Актуальное Доп соглашение_расторжение договора расположено в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_13':
        bot.send_message(call.message.chat.id, 'Актуальные Сетевые соглашения (ДОХ, РАСХ) расположены в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'recommended_forms_of_contracts_14':
        bot.send_message(call.message.chat.id, 'Актуальное Соглашение о сотрудничестве расположено в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Рекомендованные формы договоров')
    elif call.data == 'contract_work_5':
        get_standard_forms_of_contract_agreements_menu(call.message)
    elif call.data == 'standard_forms_of_contract_agreements_1':
        bot.send_message(call.message.chat.id, 'Актуальный агентский договор_МПГ расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_2':
        bot.send_message(call.message.chat.id, 'Актуальный Договор на оказание услуг таможенного представителя_доходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_3':
        bot.send_message(call.message.chat.id, 'Актуальный Договор на перевозки грузов автомобильным транспортом_расходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_4':
        bot.send_message(call.message.chat.id, 'Актуальный Договор об оказании услуг по организации диспетчерского сопровождения подвижного состава (грузовой шаттл)_доходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_5':
        bot.send_message(call.message.chat.id, 'Актуальный Договор транспортной экспедиции (МПГ)_доходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_6':
        bot.send_message(call.message.chat.id, 'Актуальный Договор транспортной экспедиции _доходный (с резидентом РФ) расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_7':
        bot.send_message(call.message.chat.id, 'Актуальный Договор транспортной экспедиции_доходный (с НЕрезидентом РФ)  РУС_АНГЛ // РУС_КИТ //  РУС_АНГЛ_КИТ расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_8':
        bot.send_message(call.message.chat.id, 'Актуальный Договор транспортной экспедиции_доходный (с НЕрезидентом РФ)_одноязычный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_9':
        bot.send_message(call.message.chat.id, 'Актуальный Договор_предоставление ПС_расходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_10':
        bot.send_message(call.message.chat.id, 'Актуальный Договор_ТЭО_расходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_11':
        bot.send_message(call.message.chat.id, 'Актуальный Договор_ТЭО_транспортеры_с услугами ТП_доходный расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_12':
        bot.send_message(call.message.chat.id, 'Актуальное Доп. соглашение к договору ТЭО_на таможенные услуги в 1С:Документооборот расположено по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_13':
        bot.send_message(call.message.chat.id, 'Актуальное ДС_об особенностях оказания услуг в вагонах-транспортерах в 1С:Документооборот расположено по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_14':
        bot.send_message(call.message.chat.id, 'Актуальное Соглашение о конфиденциальности и неразглашении информации в 1С:Документооборот расположено по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_15':
        bot.send_message(call.message.chat.id, 'Актуальное Соглашение об отсрочке в 1С:Документооборот расположено по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_16':
        bot.send_message(call.message.chat.id, 'Актуальное Соглашение об электронном документообороте в 1С:Документооборот расположено по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_17':
        bot.send_message(call.message.chat.id, 'Актуальный Типовой ДТЭ _Агроэкспресс_оферта в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_18':
        bot.send_message(call.message.chat.id, 'Актуальный Типовой ДТЭ _Агроэкспресс_оферта в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_19':
        bot.send_message(call.message.chat.id, 'Актуальный Типовой ТЭО расходный с нерезидентом РУС // РУС_АНГЛ // РУС_КИТ в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == 'standard_forms_of_contract_agreements_20':
        bot.send_message(call.message.chat.id, 'Актуальный Типовой ТЭО с таможенными услугами доходный с резидентом в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Типовые формы договоров, соглашений')
    elif call.data == '4':
        get_procurement_menu(call.message)
    elif call.data == 'procurement_1':
        bot.send_message(call.message.chat.id, 'Актуальные регламентирующие документы расположены в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Закупки - Регламентирующие документы ')
    elif call.data == 'procurement_2':
        bot.send_message(call.message.chat.id, '-------')
    #типовые формы договоров
    elif call.data == '6':
        get_quality_service_menu(call.message)
    #внешний аудит, внутренний аудит, Изменения, несоответствия, Цели по качеству
    elif call.data == 'quality_service_5':
        get_standard_operating_procedures_menu(call.message)
    elif call.data == 'standard_operating_procedures_1':
        bot.send_message(call.message.chat.id, 'Актуальный Перечень утвержденной докуменации СМК и СЭМ, СОП Приложение № 1 к СОП-18 версия 01 в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_2':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-07-Требования к санитарному состоянию оборудования при транспортировке фарм.продукции версия 01 в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_3':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-08-Требования к санитарному состоянию оборудования при транспортировке фарм.продукции версия 01 в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_4':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-10-Порядок работы с системой сигнализации, оповещения и слежения в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_5':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-10-Порядок работы с системой сигнализации, оповещения и слежения в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_6':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-13-Требования к поверке средств измерений версия 01 в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_7':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-16-Требования к процессу транспортировке фармацевтической продукции версия 01 в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_8':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-17-Правила ведения документированной информации версия 01 в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_9':
        bot.send_message(call.message.chat.id, 'Актуальные СОП-18-Правила ведения документированной информации версия 01 в 1С:Документооборот расположены по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_10':
        bot.send_message(call.message.chat.id, 'Актуальный СОП-20-Порядок проведения анализа видов и последствий рисков версия 01 в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_11':
        bot.send_message(call.message.chat.id, 'Актуальный СОП-21-Минимизация рисков контаминации ЛС при перевозке версия 01 в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_12':
        get_loading_procedure_menu(call.message)
    elif call.data == 'loading_procedure_1':
        bot.send_message(call.message.chat.id, 'Актуальный СОП-22-Порядок погрузки в реф.контейнеры АО «РЖД Логистика» версия 01 в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'loading_procedure_2':
        bot.send_message(call.message.chat.id, 'Актуальный СОП-22-Порядок погрузки в реф.контейнеры АО «РЖД Логистика» версия 02 в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == 'standard_operating_procedures_13':
        bot.send_message(call.message.chat.id, 'Актуальный СОП-22-Порядок погрузки в реф.контейнеры АО «РЖД Логистика» версия 02 в 1С:Документооборот расположен по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Служба качества - Стандартные операционные процедуры (СОП)')
    elif call.data == '7':
        get_insurance_menu(call.message)
    elif call.data == 'local_insurance_1':
        bot.send_message(call.message.chat.id, 'Актуальная Корпоративная концепция страховой защиты компании Холдинга "РЖД" расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Страхование')
    elif call.data == 'local_insurance_2':
        bot.send_message(call.message.chat.id, 'Актуальная информация о Страховании грузов расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Страхование')
    elif call.data == 'local_insurance_3':
        bot.send_message(call.message.chat.id, 'Актуальная информация о Страхованиии ответственности_РЖДЛ расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Страхование')
    elif call.data == '8':
        get_constituent_documents_menu(call.message)
    elif call.data == 'constituent_documents_1':
        bot.send_message(call.message.chat.id, 'Актуальный список Аффилированных лиц расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Аффилированные лица')
    elif call.data == 'constituent_documents_2':
        bot.send_message(call.message.chat.id, 'Актуальный список Бенефициаров расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Бенефициары')
    elif call.data == 'constituent_documents_7':
        bot.send_message(call.message.chat.id, 'Актуальные Документы об учреждении расположены в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Документы об учреждении')
    elif call.data == 'constituent_documents_5':
        bot.send_message(call.message.chat.id, 'Актуальную выписку из ЕГРЮЛ можно скачать самостоятельно с сайта ФНС России - http://egrul.nalog.ru')
    elif call.data == 'constituent_documents_9':
        get_licenses_certificates_permissions_menu(call.message)
    elif call.data == 'licenses_certificates_permissions_1':
        bot.send_message(call.message.chat.id, 'Актуальная Лицензия_ПРР_опасные грузы расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Лицензии, сертификаты, разрешения')
    elif call.data == 'licenses_certificates_permissions_2':
        bot.send_message(call.message.chat.id, 'Актуальное Свидетельство СРО расположено в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Лицензии, сертификаты, разрешения')
    elif call.data == 'licenses_certificates_permissions_3':
        bot.send_message(call.message.chat.id, 'Актуальная Таможенная лицензия расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Лицензии, сертификаты, разрешения')
    elif call.data == 'licenses_certificates_permissions_4':
        bot.send_message(call.message.chat.id, 'Актуальная Лицензия_гостайна расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Лицензии, сертификаты, разрешения')
    elif call.data == 'constituent_documents_11':
        get_powers_of_the_general_director_menu(call.message)
    elif call.data == 'powers_of_the_general_director_3':
        bot.send_message(call.message.chat.id, 'Актуальные полномочия Генерального директора  расположены в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Полномочия Генерального директора')
    # валентиник, муреев 2020. соколов
    elif call.data == 'constituent_documents_13':
        get_registration_certificates_menu(call.message)
    elif call.data == 'registration_certificates_1':
        bot.send_message(call.message.chat.id, 'Актуальный лист записи из ЕГРЮЛ об изменении наименования Общества расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Свидетельства о регистрации')
    elif call.data == 'registration_certificates_2':
        bot.send_message(call.message.chat.id, 'Актуальные свидетельства о регистрации Общества расположены в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Свидетельства о регистрации')
    elif call.data == 'constituent_documents_17':
        bot.send_message(call.message.chat.id, 'Актуальный Устав Общества расположен в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Учредительные документы - Устав')
    #Бухгалтерская отчетность, Внутренние документы, ДЗО, Ежеквартальные отчеты,ОАО РЖД, Санкции, Совет директоров, Комитеты, Список акционеров, Филиалы
    elif call.data == '9':
        calculators_menu(call.message)
    elif call.data == 'calculators_1':
        bot.send_message(call.message.chat.id, 'https://msk.arbitr.ru/process/duty/calc')
    elif call.data == 'calculators_2':
        bot.send_message(call.message.chat.id, 'https://vsrf.ru/lk/calculator/list')
    elif call.data == 'calculators_3':
        bot.send_message(call.message.chat.id, 'https://dogovor-urist.ru/calculator/dogovor_neustoyka/')
    elif call.data == 'calculators_4':
        bot.send_message(call.message.chat.id, 'https://dogovor-urist.ru/calculator/395gk/')
    elif call.data == 'calculators_5':
        bot.send_message(call.message.chat.id, 'https://dogovor-urist.ru/calculator/indeksatsiya_208gpk/')

# Обработка входящих текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получение текста сообщения
    message_text = message.text.lower()

    # Проверка наличия ключевых слов и отправка соответствующего ответа

    if 'согласовывает' in message_text or 'согласующие' in message_text or 'согласование договора' in message_text or 'согласование в 1с' in message_text or 'список согласующих' in message_text:
        bot.send_message(message.chat.id, 'Договоры, дополнительные соглашения, протоколы согласования договорной цены в обязательном порядке согласовывают: Непосредственный руководитель автора документа, Профильный директор, Главный бухгалтер, Начальник службы расчетов (только нетиповые), Директор по экономике и финансам (в определенных ЛНА случаях), Отдел безопасности, Отдел правового обеспечения (только нетиповые), Отдел управления закупками (в случае расходного договора), Директор по правовым вопросам (в случае расходного договора), Директор по снабжению и закупочной деятельности (в случае расходного договора)')
    elif 'нерезидент' in message_text or 'документы' in message_text or 'контрагента' in message_text:
        bot.send_message(message.chat.id, 'Список документов по конкретным юрисдикциям размещен в памятке по Договорной работе с иностранными контрагентами которая расположена в 1С:Документооборот по следующему адресу: Внутренние документы - Портал внутренней корпоративной информации - Договорная работа - Полезное. Если в списке отсутствует страна регистрации контрагента - по общему правилу руководствуемся списком документов, предусмотренным действующим Положением о договорной работе (Приложение 2, графы по нерезидентам юридическим лицам и физическим лицам). Если вы не нашли ответ на свой вопрос можете обратиться в отдел правого обеспечения')
    elif 'молочная продукция' in message_text or 'перевозка молока' in message_text:
        bot.send_message(message.chat.id, 'Согласно ГОСТ 31450-2013 и ГОСТ Р 53914-2010- ультрапастеризованное молоко и молочные коктейли (молочный напиток) транспортируются специализированными транспортными средствами в соответствии с правилами перевозок скоропортящихся грузов, действующими на транспорте конкретного вида. Транспортировка сухого молока допускается в универсальном металлическом контейнере по ГОСТ 15102, с особенностями, предусмотренными ГОСТ 10970-87.')
    elif 'безвозмездный' in message_text or 'субаренды' in message_text:
        bot.send_message(message.chat.id, 'Юридического запрета на заключение безвозмездного договора передачи имущества во временное пользование нет, однако квалифицировать такие сделки необходимо как договоры безвозмездного пользования (ссуды). При заключении такой сделки необходимо удостовериться в полномочиях контрагента на передачу имущества, предусмотреть ряд условий, нивелирующих риск признания сделки ничтожной, а также отразить необходимые для АО «РЖД Логистика» условия и отличающиеся от соответствующих общих положений, предусмотренных для договоров аренды (в т.ч. по ремонту и содержанию имущества, ответственности за него, требования о его передаче, риска случайной гибели).')
    elif 'товарный знак' in message_text or 'размещение' in message_text:
        bot.send_message(message.chat.id, 'Использование чужого товарного знака в информационных целях возможно при условии, что использующее лицо не создает видимость того, что оно выступает под спорным товарным знаком. Однако из-за неоднородной судебной практики существует риск неблагоприятных правовых последствий, в том числе денежных штрафов и компенсаций. В связи с этим рекомендовано получать письменное согласие на его использование.')
    elif 'аренда' in message_text or 'недвижимость' in message_text or 'регистрация' in message_text or 'договор аренды' in message_text:
        bot.send_message(message.chat.id, 'Государственной регистрации подлежит договор аренды здания или сооружения, заключенный на срок НЕ менее 1 года. Если далее договор пролонгируется менее чем на 1 год, либо  возобновляется  на неопределенный срок (т.е. стороны продолжают исполнять свои обязательства по нему без соглашения о продлении на какой-либо конкретный срок), в этом случае государственная регистрация не требуется. Чаще всего во избежание необходимости такие договоры заключаются на 11 месяцев.')
    elif 'счет' in message_text or 'счёт' in message_text or 'счет-оферта' in message_text or 'счёт-оферта' in message_text or 'расходный договор' in message_text:
        bot.send_message(message.chat.id, 'Оплата по счету/счету-оферте является заключением договора конклюдентными (фактическими) действиями. РЖДЛ заключает расходные договоры, в том числе путем оплаты счета, счета-оферты? в рамках Закона № 223-ФЗ. Такие договоры также подлежат согласованию в системе документооборота общества согласно локальным нормативным актам РЖДЛ.')
    elif 'take or pay' in message_text or 'бери или плати' in message_text or 'гарантированный объем' in message_text or 'гарантированный объём' in message_text:
        bot.send_message(message.chat.id, 'Take or pay - условие, которое стороны могут предусмотреть в договоре для фиксации минимального гарантированного объема услуг/товаров. В рамках ТЭО это означает, что экспедитор берёт на себя обязательство оказать зафиксированный в договоре (ДС) минимальный объём услуг, а клиент обязуется в любом случае оплатить этот объём, вне зависимости от того, сколько услуг он на самом деле заказал в рассматриваемый период, т.е. независимо от объема фактически оказанных услуг.')
    elif 'эдо' in message_text or 'эцп' in message_text or 'доверенность' in message_text:
        bot.send_message(message.chat.id, 'Оформление отдельной доверенности на подписание документов по ЭДО с помощью ЭЦП не требуется. Электронно цифровая подпись (ЭЦП) является аналогом собственноручной подписи, специального полномочия на использование ЭЦП не требуется, т.к. это право принадлежит самому обладателю подписи.')
    elif 'ставка' in message_text or 'ставки' in message_text or 'одностороннее изменение' in message_text:
        bot.send_message(message.chat.id,
                         'Не исключать. Необходимо указать ограничение по невозможности изменения стоимости по Поручением, принятым Экспедитором к исполнению и по которому уже начато оказание услуг по Договору')
    elif 'снижение' in message_text or 'исключение' in message_text or 'штраф' in message_text:
        bot.send_message(message.chat.id,
                         'Снижение или исключение штрафа 10% сверх от понесенных Экспедитором расходов допускается в случае если Клиентом принимаются без изменений  пункт 5.5. Договора')
    elif 'возврат траспортных средств' in message_text or 'возврату транспортных средств' in message_text:
        bot.send_message(message.chat.id,
                         'Если оказываются только платежно-финансовые услуги - возможно исключить. Если по договору обязанности Экспедитора подразумевают только предоставление транспортных средств - не исключать.')
    elif 'осмотр' in message_text or 'техническая пригодность' in message_text or 'осмотру' in message_text or 'коммерческая пригодность' in message_text or 'коммерческой пригодности' in message_text:
        bot.send_message(message.chat.id,
                         'Не исключать. Осмотр транспортного средства на предмет его годности в коммерческом отношении для перевозки заявленного груза может осуществить только грузоотправитель, как лицо, обладающее наиболее полной информацией об отправляемом грузе.')
    elif 'очистка вагонов' in message_text or 'очистке вагонов' in message_text:
        bot.send_message(message.chat.id,
                         'Не исключать. Исключение возможно только когда Экспедитор оказывает такую услугу. Обязанность по очистке подвижного состава после выгрузки предусмотрена ст. 44 УЖТ и лежит на грузополучателе.')
    elif 'односторонний зачет' in message_text or 'односторонний зачёт' in message_text:
        bot.send_message(message.chat.id,
                         'Не исключать. Право одностороннего зачета дает право Экспедитору возмещать задолженности за ранее оказанные услуги, по которым, в том числе, может истекать срок исковой давности.')
    elif 'удержание груза' in message_text or 'удержании груза?' in message_text or 'удержании груза' in message_text:
        bot.send_message(message.chat.id,
                         'Возможно исключение в случае при наличии 100% предоплаты и оказания Экспедитором платежно-финансовых услуг или услуг по предоставлению подвижного состава.')
    elif 'исключить' in message_text or 'возмещение' in message_text or 'расходы' in message_text or 'ответственность клиента' in message_text:
        bot.send_message(message.chat.id,
                         'Если Вас интересует возможность исключения ответственности клиента  в виде возмещения дополнительных расходов экспедитора, то исключение данного условия договора не допускается. Обязанность по возмещению Клиентом всех расходов Экспедитора императивно указана в ФЗ О ТЭД и подтверждена судебной практикой.')
    elif 'коэффициент' in message_text or 'ндс' in message_text or 'ндс 0%' in message_text:
        bot.send_message(message.chat.id, 'Предусмотренный договором коэффициент 2,6 представляет собой прямые затраты РЖДЛ, заключающиеся в следующем: в случае непредставления Клиентом документов в срок, установленный п. 9 ст. 165 НК РФ, Клиент уплачивает Исполнителю: 1) сумму НДС по ставке 20%, исчисленную от стоимости оказанных услуг, по которым применение ставки НДС 0% не подтверждено, и сумму штрафа. 2) пеня за каждый календарный день просрочки исполнения обязанности по уплате налога определяется в процентах от неуплаченной суммы налога (пени 1/300 от ключевой ставки ЦБ РФ * за 30 дней, 1/150 последующие дни); 3)возмещение суммы налога на прибыль с начисленного штрафа Клиенту; 4)прочие расходы РЖДЛ, связанные с неисполнением обязанности Клиента по предоставлению документов в срок, установленный п.9 ст. 165 НК РФ. 5) штрафы от соисполнителей')
    elif 'ндс 0%' in message_text or 'ставка ндс' in message_text or 'международная перевозка' in message_text or 'транзит' in message_text or 'ставку' in message_text:
        bot.send_message(message.chat.id, 'Ставка НДС 0% может применяться РЖДЛ при оказании следующих услуг: 1) транспортно-экспедиционных услуг (ТЭО) при организации: - международной перевозки товаров на основании договора ТЭО; - транзитной жд перевозки товаров, порожнего жд подвижного состава или контейнеров по РФ на основании договора ТЭО из одного иностранного государства в другое; - жд перевозки экспортируемых (реэкспортируемых) товаров. *Международной является ﻿перевозка товаров, при которой пункт отправления или пункт назначения товаров расположен за пределами территории РФ. 2) предоставления жд подвижного состава и (или) контейнеров для: - международных перевозок товаров; - транзитных жд перевозок товаров через территорию РФ из одного иностранного государства в другое; - жд перевозки экспортируемых (реэкспортируемых) товаров. 3) услуг (работ), непосредственно связанных с перевозкой или транспортировкой по РФ иностранных товаров, которые помещены под таможенную процедуру таможенного транзита. *Услугами ТЭО в целях применения НДС 0% признаются участие в переговорах по заключению контрактов купли-продажи товаров, оформление документов, прием и выдача грузов, разработка документов для проектных перевозок, организация и выполнение перевозки грузов, завоз-вывоз грузов, погрузочно-разгрузочные и складские услуги, информационные услуги, подготовка и дополнительное оборудование транспортных средств, услуги по организации страхования грузов, платежно-финансовых услуг, услуги по таможенному оформлению грузов и транспортных средств, экспедиторское сопровождение, а также разработка и согласование технических условий погрузки и крепления грузов, розыск груза после истечения срока доставки, контроль за соблюдением комплектной отгрузки оборудования, перемаркировка грузов, обслуживание и ремонт универсальных контейнеров грузоотправителей, обслуживание рефрижераторных контейнеров и хранение грузов в складских помещениях и на открытых площадках экспедитора')
    elif 'последняя миля' in message_text or 'ндс 0%' in message_text or 'ставка ндс' in message_text or 'автоперевозка' in message_text:
        bot.send_message(message.chat.id, 'Если услуги по международной перевозке товаров (организации перевозки) выступают и оформляются в качестве части единого процесса перевозки экспортного (импортного) товара за пределы (с) территории РФ, то возможно применение ставки НДС 0%. Международный характер должен прослеживаться в доукментах по соответствующей перевозке. В ином случае, если перевозка (организация перевозки) осуществлялась только в границах территории РФ без подтверждения факта экспортного (импортного) характера применяется НДС -20%.')
    elif 'чем' in message_text and (
            'форс-мажор' in message_text or 'форс мажор' in message_text or 'непреодолимая сила' in message_text or 'непреодолимой силы' in message_text or 'непреодолимой силы?' in message_text or 'тпп' in message_text or 'обстоятельства' in message_text or 'обстоятельство' in message_text or 'подтверждение' in message_text or 'доказательство ' in message_text):
        bot.send_message(message.chat.id,
                         'Если договор заключен между резидентами РФ и в соответствии с законодательством РФ, форc-мажор подтверждает уполномоченная ТПП на территории субъекта РФ (муниципального образования), на которой наступили такие обстоятельства (выдает соответствующее заключение). При внешнеторговых сделках форс-мажор подтверждает ТПП РФ (выдает  сертификат о форс-мажоре). ТПП РФ свидетельствует форс-мажор: наступивший на территории РФ, введение иностранным государством запретов и ограничений в области предпринимательской деятельности, осуществления валютных операций, а также иных ограничительных и запретительных мер, действующих в отношении РФ или российских хозяйствующих субъектов, если такие меры повлияли на выполнение ими обязательств по внешнеторговым сделкам, когда документально подтверждено, что на территории иностранного государства компетентный орган, подтверждающий событие, препятствующее российскому хозяйствующему субъекту выполнить обязательство по внешнеторговой сделке, или осуществляющий функцию по свидетельствованию форс-мажора, прекратил свою деятельность.')
    elif 'какие' in message_text and (
            'форс-мажор' in message_text or 'форс мажор' in message_text or 'форс-мажором' in message_text or 'форс мажором' in message_text or 'непреодолимая сила' in message_text or 'непреодолимой силы' in message_text or 'непреодолимой силы?' in message_text or 'тпп' in message_text or 'обстоятельствами' in message_text or 'обстоятельства' in message_text or 'обстоятельство' in message_text or 'подтверждение' in message_text or 'доказательство ' in message_text):
        bot.send_message(message.chat.id,
                         'Если условиями договора прямо не предусмотрено иное, Форс-мажором признаются чрезвычайные, непредвиденные и непредотвратимые обстоятельства, возникшие в течение реализации договорных (контрактных) обязательств, которые нельзя было разумно ожидать при заключении договора (контракта), либо избежать или преодолеть, а также находящиеся вне контроля сторон такого договора (контракта). В частности, могут быть признаны: стихийные бедствия (землетрясение, наводнение, ураган), пожар, массовые заболевания (эпидемии), забастовки, военные действия, террористические акты, диверсии, ограничения перевозок, запретительные меры государств, запрет торговых операций, в том числе с отдельными странами, вследствие принятия международных санкций и другие, не зависящие от воли сторон договора (контракта) обстоятельства. НЕ могут быть признаны форс-мажором: предпринимательские риски(нарушение обязанностей со стороны контрагентов должника, отсутствие на рынке нужных для исполнения обязательств товаров, отсутствие у должника необходимых денежных средств), финансово-экономический кризис, изменение валютного курса, девальвация национальной валюты, преступные действия неустановленных лиц.')
    else:
        bot.send_message(message.chat.id, 'Извините, не могу найти ответ на ваш вопрос.')


# Запускаем бота
bot.polling()
