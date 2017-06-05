# -*- coding: utf-8 -*-

import sys
from sqlalchemy import Column, String, Float, create_engine
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

reload(sys)
sys.setdefaultencoding('utf-8')

Base = declarative_base()


class User(Base):
    __tablename__ = 'customers'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(20))
    identifier = Column(String(20))
    relationship = Column(String(20))
    head_identifier = Column(String(20))


class BankData(Base):
    __tablename__ = 'credits'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    customer = Column(String(20))
    daily_deposit = Column(Float)
    loan_balance = Column(Float)
    credit_card_limit = Column(Float)
    is_sms = Column(String(20))
    is_phone = Column(String(20))
    stars = Column(String(20))
    phone_number = Column(String(20))
    branch = Column(String(20))


class DBOperator(object):
    def __init__(self):
        super(DBOperator, self).__init__()
        engine = create_engine('mysql+mysqlconnector://root:admin@localhost:3306/bank_data')
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def add_user(self, user):
        query_user = self.session.query(User).filter(User.identifier == user.identifier).all()
        if not query_user:
            self.session.add(user)
            self.session.commit()

    def add_users(self, users):
        for user in users:
            query_user = self.session.query(User).filter(User.identifier == user.identifier).all()
            if not query_user:
                self.session.add(user)
        self.session.commit()

    def add_bank_data(self, bank_data):
        query_bank_data = self.session.query(BankData).filter(BankData.customer == bank_data.customer).all()
        if not query_bank_data:  # 未找到则直接增加
            self.session.add(bank_data)
        else:  # 已经找到，则取出id进行更新
            self.session.query(BankData).filter(BankData.customer == bank_data.customer).update({
                BankData.branch: bank_data.branch, BankData.daily_deposit: bank_data.daily_deposit,
                BankData.loan_balance: bank_data.loan_balance, BankData.credit_card_limit: bank_data.credit_card_limit,
                BankData.phone_number: bank_data.phone_number, BankData.is_phone: bank_data.is_phone,
                BankData.is_sms: bank_data.is_sms})
        self.session.commit()

    def add_bank_datas(self, bank_datas):
        for bank_data in bank_datas:
            query_bank_data = self.session.query(BankData).filter(BankData.identifier == bank_data.identifier).all()
            if not query_bank_data:  # 未找到则直接增加
                self.session.add(bank_data)
            else:  # 已经找到，则取出id进行更新
                pass
        self.session.commit()

if __name__ == '__main__':
    db_operator = DBOperator()
    new_user = User(name='Bob1', identifier='350823198805200013', relationship='户主',
                    head_identifier='350823198805200013')

    bank_data = BankData(customer='350823198805200013', daily_deposit=1.2, loan_balance=6000,
                         credit_card_limit=10000, is_sms='1', is_phone='1', stars='5',
                         phone_number='13159208608', branch='槟榔支行')

    db_operator.add_user(new_user)
    db_operator.add_bank_data(bank_data)

