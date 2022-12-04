from utils import load_candidates_from_json, get_candidates, get_candidates_by_name, get_candidates_by_skill

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def candidates():
    return render_template('list.html', items=load_candidates_from_json())


@app.route('/candidate/<int:x>')
def candidate_profile(x):
    name = get_candidates(x)[0]
    cand_id = get_candidates(x)[1]
    skills = get_candidates(x)[2]
    image = get_candidates(x)[3]
    return render_template('card.html', name=name, id=cand_id, img=image, skills=skills)


@app.route('/search/<candidate_name>')
def candidates_by_name(candidate_name):
    candidates_list = get_candidates_by_name(candidate_name)
    return render_template('search.html', items=candidates_list, numb=len(candidates_list))


@app.route('/skill/<skill_name>')
def candidates_by_skill(skill_name):
    candidates_list = get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=candidates_list, numb=len(candidates_list), skill=skill_name)


app.run()
