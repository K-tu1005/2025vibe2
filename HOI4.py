### 🌍 전체 통합 예시: HoI4 스타일 "2차 세계대전" 기본 설정 코드 (한국은 식민지 상태) ###

# 1. 국가 정의 (한국 제외) — 한국은 일본 식민지 상태로 설정됨
# KOR 국가 정의 제거됨

# 2. 초기 설정 (한국 없음)
# history/countries/KOR - Korea.txt 제거됨

# 3. 서울 지역 설정 (일본 소유)
history/states/386 - Seoul.txt
state = {
  id = 386
  name = "STATE_SEOUL"
  manpower = 300000
  owner = JAP
  add_core_of = JAP

  buildings = {
    civilian_factory = 2
    infrastructure = 3
  }
}

# 4. 포커스 트리 — 한국 없음
# common/national_focus/KOR.txt 제거됨

# 5. 2차 대전 세력
common/factions/00_factions.txt
faction = {
  name = "Allies"
  icon = GFX_faction_allies
}

faction = {
  name = "Axis"
  icon = GFX_faction_axis
}

faction = {
  name = "Comintern"
  icon = GFX_faction_comintern
}

# 6. 2차 대전 시작 이벤트
events/ww2_start.txt
country_event = {
  id = ww2.1
  title = "The World at War"
  desc = "Germany has invaded Poland. A global war begins."

  trigger = {
    date > 1939.9.1
    POL = { has_war_with = GER }
  }

  option = {
    name = "Prepare for total war"
    ENG = { join_faction = Allies }
    FRA = { join_faction = Allies }
    SOV = { join_faction = Comintern }
    USA = { add_opinion_modifier = { target = ENG modifier = positive_15 } }
  }
}

# 7. 2차 대전 관련 결정
common/decisions/ww2_decisions.txt
decision = {
  name = "Mobilize for War"
  visibility = { has_government = democratic }
  allow = {
    has_political_power > 100
    NOT = { has_war = yes }
  }
  effect = {
    add_political_power = -100
    add_war_support = 0.2
  }
}

# 8. 군사 템플릿 — 한국 없음 + 주요국 추가 (SIA~FRA)
common/units/division_templates/SIA.txt
division_template = {
  name = "Siamese Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    artillery = { x = 1 y = 1 }
  }
}

common/units/division_templates/BRA.txt
division_template = {
  name = "Brazilian Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    engineer = { x = 1 y = 0 }
  }
}

common/units/division_templates/ARG.txt
division_template = {
  name = "Argentine Mountain Division"
  regiments = {
    mountaineers = { x = 3 y = 2 }
    support_artillery = { x = 1 y = 0 }
  }
}

common/units/division_templates/MEX.txt
division_template = {
  name = "Mexican Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
  }
}

common/units/division_templates/ITA.txt
division_template = {
  name = "Italian Alpine Division"
  regiments = {
    mountaineers = { x = 3 y = 2 }
    support_artillery = { x = 1 y = 0 }
  }
}

common/units/division_templates/GER.txt
division_template = {
  name = "Wehrmacht Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    artillery = { x = 1 y = 1 }
    engineer = { x = 1 y = 0 }
  }
}

common/units/division_templates/JAP.txt
division_template = {
  name = "Imperial Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    support_artillery = { x = 1 y = 0 }
  }
}

common/units/division_templates/USA.txt
division_template = {
  name = "US Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    artillery = { x = 1 y = 1 }
    engineer = { x = 1 y = 0 }
  }
}

common/units/division_templates/SOV.txt
division_template = {
  name = "Red Army Rifle Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    support_artillery = { x = 1 y = 0 }
  }
}

common/units/division_templates/ENG.txt
division_template = {
  name = "British Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    engineer = { x = 1 y = 0 }
  }
}

common/units/division_templates/FRA.txt
division_template = {
  name = "French Infantry Division"
  regiments = {
    infantry = { x = 3 y = 3 }
    support_artillery = { x = 1 y = 0 }
  }
}

# 9. AI 전략 — 한국 없음
# common/ai_strategy_plans/KOR.txt 제거됨

# 10. 국가 설정 요약 (2차 대전 시기 정당명 및 이념 조정)

## 중국 공산당 (PRC)
PRC = {
  ideology = communism
  ruling_party = communism
  parties = {
    communism = { name = "중국공산당", popularity = 80 }
    neutrality = { name = "국민당", popularity = 15 }
  }
}

## 시암 (SIA)
SIA = {
  ideology = neutrality
  ruling_party = neutrality
  parties = {
    neutrality = { name = "왕실 정부", popularity = 90 }
    communism = { name = "공산주의 운동", popularity = 5 }
  }
}

## 브라질 (BRA)
BRA = {
  ideology = neutrality
  ruling_party = neutrality
  parties = {
    neutrality = { name = "군사정부", popularity = 60 }
    communism = { name = "브라질 공산당", popularity = 20 }
  }
}

## 아르헨티나 (ARG)
ARG = {
  ideology = neutrality
  ruling_party = neutrality
  parties = {
    neutrality = { name = "군부", popularity = 70 }
    democracy = { name = "공화당", popularity = 25 }
  }
}

## 멕시코 (MEX)
MEX = {
  ideology = democracy
  ruling_party = democratic
  parties = {
    democratic = { name = "혁명제도당", popularity = 80 }
    communism = { name = "사회주의 연합", popularity = 10 }
  }
}

## 이탈리아 (ITA)
ITA = {
  ideology = fascism
  ruling_party = fascism
  parties = {
    fascism = { name = "국가파시스트당", popularity = 75 }
    communism = { name = "이탈리아 공산당", popularity = 20 }
  }
}

## 독일 (GER)
GER = {
  ideology = fascism
  ruling_party = fascism
  parties = {
    fascism = { name = "국가사회주의당", popularity = 85 }
    communism = { name = "독일공산당", popularity = 10 }
  }
}

## 일본 (JAP)
JAP = {
  ideology = fascism
  ruling_party = fascism
  parties = {
    fascism = { name = "일본제국 정부", popularity = 90 }
    communism = { name = "일본공산당", popularity = 5 }
  }
}

## 미국 (USA)
USA = {
  ideology = democracy
  ruling_party = democratic
  parties = {
    democratic = { name = "민주당", popularity = 70 }
    neutrality = { name = "공화당", popularity = 25 }
    fascism = { name = "은빛 군단", popularity = 3 }
  }
}

## 소련 (SOV)
SOV = {
  ideology = communism
  ruling_party = communism
  parties = {
    communism = { name = "소련공산당", popularity = 95 }
  }
}

## 영국 (ENG)
ENG = {
  ideology = democracy
  ruling_party = democratic
  parties = {
    democratic = { name = "보수당", popularity = 60 }
    communism = { name = "영국공산당", popularity = 10 }
    fascism = { name = "브리튼 파시스트 연합", popularity = 5 }
  }
}

## 프랑스 (FRA)
FRA = {
  ideology = democracy
  ruling_party = democratic
  parties = {
    democratic = { name = "급진당", popularity = 55 }
    communism = { name = "프랑스공산당", popularity = 20 }
    fascism = { name = "프랑스 인민당", popularity = 5 }
  }
}
