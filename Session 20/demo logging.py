import logging

logging.basicConfig(
    level=logging.DEBUG,
    format= "%(asctime)s - %(filename)s - %(lineno)d - %(message)s",
    filename='test log.txt'
)

def divide(first, second):
    logging.debug(f'Gia tri tham so thu nhat la: {first}')
    logging.debug(f'Gia tri tham so thu hai la: {second}')
    result = first / second
    logging.info(f'Ket qua la: {result}')
    return result

result = divide(10,5)

# logging.debug('In ra khi đang fix bug')
# logging.info('In ra thông tin khi chạy chương trình')
# logging.warning('In ra khi có cảnh báo')
# logging.error('In ra khi có lỗi')
# logging.critical('In ra khi có tình huống nghiêm trọng')