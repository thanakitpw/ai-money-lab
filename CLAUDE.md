# Project: AI Money Mastery (E-book)

> **อัพเดตล่าสุด:** 2569-04-24 (Phase 2 production เกือบเสร็จ เหลือ layout + launch)

## ภาพรวมโปรเจกต์

สร้างและขาย e-book สอนใช้ AI หารายได้เสริม สำหรับคนไทยมือใหม่ที่ไม่มีเวลา

### ชื่อหนังสือ
> **AI Money Mastery** — *คู่มือใช้ AI สร้างรายได้เสริม สำหรับคนไม่มีเวลา*

### Brand Identity — AI Money Lab

- **Brand name:** AI Money Lab (umbrella ครอบ e-book + คอร์สอนาคต)
- **Logo:** หลอดทดลอง + $ + text (ไฟล์ `assets/book-cover.png`)
- **Color:** Navy gradient `#051A37 → #153D6F` + Gold `#FED312`
- **Font:** Kanit (Thai) + Inter (English)
- รายละเอียด: `docs/08-branding.md`

### Core Vibe (สไตล์คนไทย ที่ FB Ads ผ่าน)

- "ให้ AI ทำงานแทน" (ไม่ใช่ "ไม่ต้องขยัน" — FB Ad flag)
- "เริ่มได้ในวันเดียว" (ไม่ใช่ "เห็นผลเร็ว" — FB Ad flag)
- "ไม่ต้องเก่งเทค" / "ทำตามทีละขั้น"
- **ห้ามรับประกันรายได้เป็นตัวเลข** (FB Ad policy)

---

## Product + Pricing

### ราคา
**349 บาท** (anchor 890 — ประหยัด 61%)

### สิ่งที่ลูกค้าได้

1. **E-book AI Money Mastery** 16 บท ~180 หน้า (~40,000 คำ)
2. **AI Starter Kit** (มูลค่ารวม 1,270 บาท) — 3 ชิ้น
   - Prompt Library Pro (51 prompts)
   - Template Pack (4 templates)
   - Cheat Sheet "30 วันแรกกับ AI"

### Pricing Strategy

- **Anchor:** ปกติ 890 → โปรเปิดตัว 349
- **Bundle:** E-book + Starter Kit มูลค่า 1,270 (anchor bonus สูงกว่า main product)
- **ไม่มี money-back guarantee** — ใช้ trust signals แทน:
  - Preview เนื้อหา 3-5 หน้าฟรี
  - Testimonial + screenshot (ต้องเก็บหลัง launch)
  - Demo video
  - Member-only community
- **ไม่ A/B test ราคา** ใน Phase 1 (ล็อก 349 ไว้ 4-6 สัปดาห์)
- **Upsell:** Order bump +99, Upsell 990, Downsell 199 (เปิดหลัง validate)

---

## กลุ่มเป้าหมาย

### Primary Persona
**"คนที่อยากได้รายได้เสริม แต่ไม่มีเวลา/ไม่มีทักษะพิเศษ"**

- อายุ 28-50
- ทำงานประจำ / แม่บ้าน / คนเริ่มหารายได้เสริม
- ไม่เก่งเทค กลัว ChatGPT ใช้ไม่เป็น
- มีเงินพอจ่าย 349 ถ้าเชื่อว่าจะได้รายได้คืน

### Tier A — ยิงแอด Phase 1

1. **พนักงานประจำอายุ 30+ อยากมี Plan B**
2. **แม่บ้าน / คุณแม่ลูกเล็ก**

### Tier B — ขยาย Phase 2

3. ฟรีแลนซ์ต้องการขยายรายได้
4. คนเกษียณเร็ว / คนว่างงาน
5. นักศึกษาจบใหม่หางานไม่ได้

---

## Funnel Strategy — Community-Driven Lead Magnet

❌ ห้ามยิง FB Ad → LP → ขายตรง (CVR ต่ำ ขาดทุน)

✅ ใช้ funnel นี้:

```
FB Ad (pitch lead magnet ฟรี)
  ↓
Landing Page: "ดาวน์โหลด + เข้า community ฟรี"
  ↓
เก็บข้อมูล: ชื่อ + LINE ID + Email
  ↓
Auto-reply ส่ง:
  • ลิงก์ดาวน์โหลด lead magnet
  • รหัสเข้า LINE OpenChat (ล็อค)
  • ลิงก์เข้า Facebook Group
  ↓
Nurture 3-7 วัน (โพสต์ใน community + LINE broadcast)
  ↓
Pitch AI Money Mastery 349 บาท
```

### Community Strategy

- **LINE OpenChat (ล็อคด้วยรหัส)** — real-time chat, exclusive feel
- **Facebook Group** — discoverable, social proof, content ถาวร
- เป้าก่อน launch: ต้องมี **50-100 คนในกลุ่ม**
- LINE password ต้อง auto-send (ไม่ manual)
- Moderate 2-3 โพสต์/สัปดาห์

### Tech Stack

- **Landing page:** Systeme.io (ฟรี) / Strikingly
- **Payment + delivery:** Payhip (มี watermark per buyer)
- **Email/LINE broadcast:** LINE OA + Systeme.io
- **File delivery:** Payhip native (auto ส่งลิงก์หลังชำระ)

---

## Business Model

- Gross profit ต่อเล่ม: **~334 บาท** (หลังหัก payment fee + delivery)
- Max CPA: **140 บาท (target), 180 บาท (acceptable)**
- ต้นทุนตั้งต้น: ~40,000 บาท
- **Break-even: 123 เล่ม**
- งบ ads เริ่ม: 200-300 บาท/วัน × 14 วัน = 3,000-4,000 บาท test phase

### เป้ายอดขาย
- M1: 50-100 เล่ม | M3: 200-400 | M6: 500-800

---

## โครงสร้างไฟล์

```
e-book/
├── CLAUDE.md                     ← ไฟล์นี้
├── checklist.md                  ← งานที่เหลือ + log
├── .gitignore
├── docs/                         ← Strategy + brand + guides (10 ไฟล์)
│   ├── 01-overview.md            → ภาพรวม
│   ├── 02-market-research.md     → คู่แข่งและ gaps
│   ├── 03-pricing-business.md    → ราคา + break-even
│   ├── 04-funnel-community.md    → funnel + LINE/FB
│   ├── 05-book-outline.md        → outline 16 บท
│   ├── 06-lead-magnet-starter-kit.md
│   ├── 07-writing-plan.md
│   ├── 08-branding.md            → Brand kit: สี/font/logo
│   ├── 09-canva-layout-guide.md  → วิธีจัด Canva step-by-step
│   └── proofreading-report.md
├── manuscript/                   ← ต้นฉบับ 16 บท (.md)
│   ├── part-1/   Ch 1-4
│   ├── part-2/   Ch 5-8
│   ├── part-3/   Ch 9-15
│   └── appendix/ Ch 16
├── manuscript-full.md            ← merged เล่มเต็ม
├── lead-magnet/
│   └── lead-magnet.md            ← คู่มือฟรี 25 หน้า
├── starter-kit/
│   ├── prompt-library.md         ← 51 prompts
│   ├── template-pack.md          ← spec (ต้องทำ Canva จริง)
│   └── cheat-sheet.md            ← 30 วัน print-ready
├── assets/
│   └── book-cover.png            ← ปกหนังสือ (AI-generated)
├── scripts/
│   ├── generate_pdf.py           ← Python + weasyprint
│   └── style.css                 ← CSS navy/gold + Kanit
└── final/                        ← Output
    ├── AI-Money-Mastery.docx     ← ไฟล์ Word สำหรับ Canva import
    ├── sample-ch01.docx
    └── sample-ch01.pdf           ← Sample ตรวจคุณภาพ
```

---

## สถานะปัจจุบัน (2569-04-24)

### ✅ Phase 1 — Market Validation (ครบ 100%)
- [x] หัวข้อ: AI สำหรับมือใหม่
- [x] ชื่อ: AI Money Mastery (+pivot money angle)
- [x] ราคา: 349 บาท + anchor 890
- [x] กลุ่มเป้าหมาย: คนอยากได้รายได้เสริม / ไม่มีเวลา
- [x] สำรวจคู่แข่งในไทย (Data-Espresso, Benzio, Skooldio ฯลฯ)
- [x] Pricing + discount strategy
- [x] Business model + break-even 123 เล่ม
- [x] Funnel design — community-driven lead magnet

### ✅ Phase 2a — Content Production (ครบ 100%)
- [x] Outline 16 บท 3 Parts + Appendix
- [x] **ต้นฉบับ 16/16 บท** ~40,000 คำ ~180 หน้า
- [x] **Proofread + แก้ 10 issues**
- [x] **Thai language cleanup** — English → ไทย 68+ จุด + ปี ค.ศ. → พ.ศ.
- [x] **Lead magnet 25 หน้า** (Ch 1+2+sneak peek Ch 10)
- [x] **Starter Kit** (2.5/3 ชิ้น)
  - Prompt Library 51 prompts ✓
  - Cheat Sheet 30 วัน ✓
  - Template Pack — มีแค่ spec ยังไม่มี Canva file จริง ⚠️
- [x] **Brand Identity** — Logo + cover + palette + fonts
- [x] **PDF generator** — Python + weasyprint (`scripts/generate_pdf.py`)
- [x] **DOCX generator** — Pandoc (`final/AI-Money-Mastery.docx`)
- [x] **Canva Layout Guide** — step-by-step (`docs/09-canva-layout-guide.md`)
- [x] **GitHub repo** — pushed to `github.com/thanakitpw/ai-money-lab`

### 🔄 Phase 2b — Layout & Finalize (กำลังทำ / คุณต้องลงมือ)
- [ ] **Layout ใน Canva** (ใช้ docx + cover + guide) — user task ~10-15 ชม.
- [ ] **Export final PDF** พร้อมขาย
- [ ] **สร้าง Canva template จริง 4 ชิ้น** (Template Pack ยังขาด)
- [ ] **Generate PDF ของ Starter Kit** (Prompt Library + Cheat Sheet)

### ⏳ Phase 3 — Pre-Launch (ยังไม่เริ่ม)
- [ ] สร้าง Facebook Page "AI Money Lab"
- [ ] สร้าง Facebook Group "AI Money Lab Insider"
- [ ] สร้าง LINE OpenChat ล็อครหัส "AI Money Lab Lounge"
- [ ] เปิด LINE Official Account @aimoneylab
- [ ] จอง IG + TikTok handle
- [ ] Seed community 50-100 คน + posts warm-up
- [ ] FB Cover + Profile Pic + IG grid starter
- [ ] Setup Payment (Payhip) + Upload files
- [ ] Landing page (Systeme.io / Strikingly)
- [ ] Email / LINE nurture sequence 7 ฉบับ

### ⏳ Phase 4 — Launch (ยังไม่เริ่ม)
- [ ] Ad creative (5-10 copy + 5-10 visual + 1-3 video)
- [ ] FB Pixel + Conversion API
- [ ] Test ads 200-300 บาท/วัน × 14 วัน
- [ ] Scale / pivot ตามผล

### ⏳ Phase 5 — Post-Launch (ยังไม่เริ่ม)
- [ ] Moderate community
- [ ] Collect testimonials
- [ ] Optimize funnel / retargeting
- [ ] Product ladder — คอร์ส / coaching ต่อ

---

## หมายเหตุสำหรับ Claude

### ภาษา
- **ตอบเป็นภาษาไทยเสมอ** (ผู้ใช้สื่อสารไทย) — รวมถึงหัวข้อ, bullet, คำอธิบาย
- คำศัพท์เทคนิค/การตลาดที่ไทยไม่มีคำเทียบ ใช้ทับศัพท์ได้ (เช่น funnel, CTR, CPM)
- **ในต้นฉบับหนังสือ** ใช้ปี พ.ศ. (ปี 2569) ไม่ใช่ ค.ศ.

### การใช้ Skills (บังคับ)
- **ทุกครั้งที่ทำงานในโปรเจกต์นี้ ต้องใช้ skill ที่เกี่ยวข้องก่อน** ห้ามตอบจากความรู้ทั่วไป
- ก่อนลงมือ ตรวจว่าขั้นตอนตรงกับ skill ใด แล้วเรียกผ่าน Skill tool
- ถ้าไม่มี skill ตรง แจ้งผู้ใช้ก่อน

### Skills ที่อนุมัติแล้ว

**Phase 1 — Market validation (ใช้เสร็จแล้ว ✓)**
- `startup-business-analyst-market-opportunity` ✓
- `competitor-alternatives` ✓
- `pricing-strategy` ✓
- `business-analyst` ✓
- `market-sizing-analysis` ✓

**Phase 2a — Content production (ใช้เสร็จแล้ว ✓)**
- `content-creator` ✓
- `beautiful-prose` ✓
- `avoid-ai-writing` ✓
- `copy-editing` ✓
- `professional-proofreader` ✓
- `pdf` / `pdf-official` (available)

**Phase 2b+ — ยังไม่อนุมัติ** (ขอก่อนใช้)
- กลุ่มยิงแอด: `paid-ads`, `ad-creative`, `copywriting`, `marketing-psychology`
- กลุ่มหน้าขาย: `landing-page-generator`, `page-cro`
- กลุ่ม launch: `launch-strategy`, `lead-magnets`, `analytics-product`
- กลุ่มอื่น: `canva-automation`, `email-sequence`, `social-content`

### Agent Teams — Workflow ที่ใช้อยู่

โปรเจกต์ใช้ `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` เปิดใน user settings
Spawn agent "Inthira" (นักเขียน) ด้วย Agent tool + name → ใช้ SendMessage คุยต่อเนื่องเพื่อเขียน consistent voice ข้ามบท

**Tip:** เวลาให้งานเขียนหนังสือ ใช้ Inthira ต่อได้ — voice บทต่อไปจะ consistent กับ 16 บทที่มี

### สไตล์การตอบ
- ผู้ใช้อาจเป็นมือใหม่ด้านการตลาด/การเขียน — อธิบายแบบ step-by-step ไม่ข้ามขั้น
- ให้คำแนะนำแบบ actionable (ทำอะไร ทำยังไง) ไม่ใช่ทฤษฎีลอย ๆ
- ถ้าต้องเลือก/ตัดสินใจ ให้เสนอ 2-3 ทางเลือกพร้อม tradeoff
- สื่อสารสั้น กระชับ — ไม่เวิ่นเว้อ

### Git Workflow
- Repo: `github.com/thanakitpw/ai-money-lab`
- Main branch: `main`
- **ต้องเป็น Private repo** — เนื้อหาในเล่มคือทรัพย์สินทางปัญญา
- Commit เมื่อ milestone สำคัญ (ไม่ต้องทุกการแก้เล็ก ๆ)
