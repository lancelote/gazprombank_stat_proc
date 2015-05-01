Gazprombank statements processing utility
==============

Simple utility for auto processing gazprombank statements (zip files) and
creating bank transfer order files for each transaction plus a summary statements
file

Небольшой скрипт для автоматической обработки выписок Газпромбанка. На входе
забирает сырые выписки в zip формате, распаковывает, отделяет часть с общей
информацией о проведенных за день платежах и добавляет в общий sum-файл,
подробную информацию по каждому платежу сохрянет в отдельных файлах,
категоризируя по дате. Дополнительно проверяет на наличие отсутствующих выписок.

**Still incomplete!**