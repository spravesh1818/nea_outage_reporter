from app import app,db
from flask import render_template,flash,redirect,url_for,request,jsonify
from app.forms import LoginForm,RegistrationForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User, Report
from werkzeug.urls import url_parse
import json
from .models import Province,District,LocalBody
from .schemas import ProvinceSchema,DistrictSchema,LocalBodySchema



@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=="GET":
        return render_template('index.html',title="Home")
    if request.method=="POST":
        print(request.form)
        return redirect('/index')


@app.route('/reports',methods=['GET','POST'])
@login_required
def reports():
    if request.method=="GET":
        all_reports=Report.query.all()
        return render_template('reports.html',title="Home",reports=all_reports)
    if request.method=="POST":
        return "Report recorded succcessfully",200

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form=LoginForm()


    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user,remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page=(url_for('index'))
        return redirect(next_page)
    return render_template('login.html',form=form,title='Sign In')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/province', methods=['GET', 'POST'])
def get_province_list():
    if request.method=="GET":
        all_provinces=Province.query.all()
        all_provinces_schema=ProvinceSchema(many=True)
        output=all_provinces_schema.dump(all_provinces)
        return jsonify(output)

@app.route('/district_by_province/<int:province_id>',methods=['GET','POST'])
def get_district_list(province_id):
    if request.method=="GET":
        all_districts = District.query.filter_by(province_id=province_id)
        all_districts_schema = DistrictSchema(many=True)
        output = all_districts_schema.dump(all_districts.values('id','name'))
        return jsonify(output)


@app.route('/localbody_by_district/<int:district_id>',methods=['GET','POST'])
def get_localbody_list(district_id):
    if request.method=="GET":
        all_localbody = LocalBody.query.filter_by(district_id=district_id)
        all_localbody_schema = LocalBodySchema(many=True)
        output = all_localbody_schema.dump(all_localbody.values('id','name'))
        return jsonify(output)

@app.route('/api/v1/report',methods=['POST'])
def add_a_report():
    response = add_report_to_db(request.form.to_dict())
    return "Report Successfully recorded",200

@app.route('/report',methods=['POST'])
def add_a_report_html():
    response=add_report_to_db(request.form.to_dict())
    flash('Your report has been recorded.If you want to report again,go ahead!')
    return redirect('/')



def add_report_to_db(data):
    province=Province.query.filter_by(id=int(data['province'])).first()
    district=District.query.filter_by(id=int(data['district'])).first()
    localbody=LocalBody.query.filter_by(id=int(data['localbody'])).first()
    report=Report(province=province.name,district=district.name,localbody=localbody.name,customer_id=data['customer_id'],latitude=data['latitude'],longitude=data['longitude'],ward=data['ward_number'],status="Reported")
    db.session.add(report)
    db.session.commit()
