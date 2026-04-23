# 09. Canva Layout Guide — AI Money Mastery

คู่มือจัด layout e-book ใน Canva ทีละขั้น เขียนเพื่อให้ทำเสร็จใน 8-12 ชั่วโมง (แบ่ง 2-3 วัน)

ใช้ไฟล์ `final/AI-Money-Mastery.docx` เป็น text source และ `assets/book-cover.png` เป็นปก

---

## ขั้นที่ 0 — เตรียมของก่อนเปิด Canva

- [ ] Canva Pro (399 บาท/เดือน) — ใช้ 1 เดือนจัดเล่มจบ แล้ว cancel ได้
- [ ] `AI-Money-Mastery.docx` เปิดค้างใน Google Docs สำหรับ copy-paste
- [ ] `assets/book-cover.png` พร้อมใช้
- [ ] Logo `AI Money Lab.png` พร้อมใช้ (Profile + inner page)

---

## ขั้นที่ 1 — สร้างไฟล์ใหม่ใน Canva

**ประเภท:** Create a design → **Custom size**

**ขนาดที่แนะนำ:**

| ขนาด | ใช้เมื่อ | หน้าจริง |
|---|---|---|
| **A5 (148 × 210 mm)** ⭐ แนะนำ | อ่านมือถือ + tablet | ~200 หน้า |
| US Letter (8.5 × 11 in) | สำหรับ print | ~130 หน้า |
| Kindle (1600 × 2560 px) | Amazon publish | ~200 หน้า |

**เลือก A5** — ขนาดมาตรฐาน e-book ไทย อ่านง่ายบนมือถือ

**จำนวนหน้าเริ่มต้น:** 1 หน้า (เพิ่มทีละหน้าระหว่างทำ)

---

## ขั้นที่ 2 — ตั้ง Brand Kit

**Menu:** Brand → Brand Kit (ต้อง Canva Pro)

### Color Palette

เพิ่มเป็น Brand Colors 6 สี

| ชื่อ | Hex | ใช้กับ |
|---|---|---|
| Navy Dark | `#051A37` | พื้นหลัง chapter title, header |
| Navy Mid | `#153D6F` | พื้นหลัง alt, sub-heading |
| Gold | `#FED312` | highlight, icon, border |
| Gold Warm | `#E5A500` | hover, secondary accent |
| Text Dark | `#1A1A2E` | body text |
| Text Subtle | `#8B95A8` | caption, footer |

### Fonts (Upload ทั้ง 2)

**Kanit** (Google Fonts ฟรี — Canva มีในตัวแล้ว)
- Heading: **Kanit Bold 700**
- Sub-heading: **Kanit SemiBold 600**
- Body: **Kanit Light 300** หรือ **Regular 400**

**Inter** (Google Fonts ฟรี — Canva มีในตัว)
- Brand marks / uppercase labels: **Inter Bold**
- Page numbers / caption: **Inter Regular**

---

## ขั้นที่ 3 — สร้าง Master Pages (6 แบบ)

สร้างเป็น template แยก → copy ใช้ทั้งเล่ม

### Master 1 — Cover (หน้าแรก)

- Upload `assets/book-cover.png` → ลากเต็มหน้า
- ไม่มี margin ไม่มี page number
- ไม่ต้องแก้อะไรเพิ่ม

### Master 2 — Inside Cover / Copyright Page

**Layout:**
- Navy BG #051A37 หรือ ขาวล้วน
- กลางหน้า: โลโก้ AI Money Lab (ขนาดเล็ก)
- ล่าง: "AI Money Mastery · ฉบับ 1.0 · ปี 2569 · © AI Money Lab"

### Master 3 — TOC (สารบัญ) — 2 หน้า

**Layout:**
- Heading "สารบัญ" สี Gold Kanit Bold 28pt
- เส้น Gold ใต้ heading
- List:
  - **Part heading** (Part 1, Part 2, Part 3, Appendix) — Kanit Bold 14pt, Navy
  - **Chapter** (บทที่ 1, 2, ...) — Kanit Regular 11pt, Text Dark
  - **Page number** ด้านขวา — Inter Regular 11pt, Gold

**Format:**
```
Part 1 — ปูพื้นฐาน AI                           [Gold underline]
  บทที่ 1  AI ไม่ใช่เรื่องเทค .................. 10
  บทที่ 2  เลือก AI ตัวไหนดี .................. 22
  ...
```

### Master 4 — Part Divider (3 หน้า — Part 1, 2, 3)

**Layout:**
- พื้นหลัง gradient Navy Dark → Navy Mid (135°)
- กลางหน้าบน:
  - Small text "PART" — Inter Bold 9pt Gold letter-spacing 8px
  - ตัวเลขใหญ่ "1" / "2" / "3" — Kanit Bold 120pt Gold
- กลางหน้ากลาง:
  - เส้น Gold 48mm
- กลางหน้ากลาง-ล่าง:
  - "ปูพื้นฐาน AI" — Kanit Bold 20pt สีขาว (เปลี่ยนตาม Part)
- ไม่มี page number, ไม่มี header

**ตัวอย่าง Part names:**
- Part 1: ปูพื้นฐาน AI
- Part 2: สกิลที่ต้องมี
- Part 3: 4 วิธีหารายได้จริง
- (Appendix ไม่ต้องมี divider ก็ได้ — ใส่หลัง Ch 15 เลย)

### Master 5 — Chapter Title Page (16 หน้า — เปิดแต่ละบท)

**Layout ตาม PDF ที่เราทำ:**
- พื้นหลัง gradient Navy Dark → Navy Mid (135°)
- เส้น Gold บน + ล่าง (48mm × 1pt)
- กลางบน: "CHAPTER" — Inter Bold 9pt Gold letter-spacing 8px
- ไอคอน ⚗ หรือ logo เล็ก — Gold 28pt
- ตัวเลขใหญ่ "01", "02", ... "16" — Kanit Bold 64pt Gold
- ชื่อบท — Kanit SemiBold 20pt สีขาว line-height 1.35
- ไม่มี page number, ไม่มี header

### Master 6 — Body / Content Page

**Layout:**
- Margin: top 20mm, bottom 22mm, left/right 18mm
- พื้นหลัง: ขาวล้วน
- **Top-right:** "AI MONEY MASTERY" — Inter Regular 6.5pt Text Subtle letter-spacing 2px
- **Footer center:** หมายเลขหน้า — Inter Regular 8pt Text Subtle

---

## ขั้นที่ 4 — ตั้ง Text Styles (Saved Styles)

Canva → Text → Styles → Create style จาก template

### Body paragraph
- Font: **Kanit Light 300**
- Size: **9.5pt**
- Line height: **1.65**
- Color: **Text Dark #1A1A2E**
- Align: **Justify**

### H2 — Section heading (e.g., "1.1 ทำไมตอนนี้...")
- Font: **Kanit Bold 700**
- Size: **14pt**
- Color: **Navy Dark #051A37**
- Margin top: 16pt / bottom: 8pt
- **Border-bottom:** 1.5pt Gold `#FED312`

### H3 — Sub-section (e.g., "### สูตร 4 ข้อ")
- Font: **Kanit SemiBold 600**
- Size: **11.5pt**
- Color: **Navy Mid #153D6F**
- Prefix: "▸ " (Gold)

### Bold inline
- Font: **Kanit SemiBold 600**
- Color: **Navy Dark**

### Bullet list
- Marker: • (Gold)
- Indent: 16pt
- Item spacing: 3pt

### Quote box (blockquote)
- Background: **#EEF2F7** (soft gray)
- Border-left: **3pt Gold #FED312**
- Padding: 10pt × 14pt
- Font: **Kanit Regular 400** (italic feel)
- Size: 9pt
- Color: **Navy Mid**

### Code block (prompt box)
- Background: **Navy Dark #051A37**
- Text color: **White**
- Font: **SF Mono** หรือ **Courier New**
- Size: 8.5pt
- Padding: 10pt
- Border radius: 5pt

### Table
- Header row: **Navy Dark #051A37** BG, White text, Kanit Bold 9pt
- Even rows: **#F5F7FA** (soft gray) BG
- Odd rows: White
- Bottom border: 1.5pt Gold
- Cell padding: 6pt

### Page number (footer)
- Font: **Kanit Regular 400** หรือ **Inter Regular**
- Size: 8pt
- Color: **Text Subtle #8B95A8**

---

## ขั้นที่ 5 — Workflow การจัด (ลำดับการใส่ content)

### Day 1 — Setup + Cover + TOC (2-3 ชั่วโมง)

1. สร้างไฟล์ Canva ใหม่ A5
2. ตั้ง Brand Kit (color + font)
3. สร้าง Master 1-3 (Cover, Copyright, TOC)
4. ยังไม่ใส่เลขหน้า TOC (ใส่ท้ายสุด)

### Day 2 — Part Dividers + Chapter Titles (3-4 ชั่วโมง)

1. สร้าง Master 4, 5
2. Duplicate Chapter Title Page 16 รอบ
3. แก้เลข + ชื่อบท ของแต่ละบท
4. แทรก Part Divider ก่อน Part 1, Part 2, Part 3

### Day 3-5 — ใส่เนื้อหาแต่ละบท (1-2 ชั่วโมง/บท)

1. เปิด Google Docs / Word ค้าง (จาก docx)
2. เปิดบทที่ 1 ของ Canva → หลัง Chapter Title Page
3. Copy ข้อความจาก docx → Paste into Canva
4. Apply saved styles: body, H2, H3
5. จัด callout / quote / table ที่เจอ
6. เพิ่มหน้าใหม่ (Add page) เมื่อเต็ม
7. ทำซ้ำสำหรับ Ch 2-16

**Tip:** ทำทีละ 2-3 บท/วัน เย็น 1-2 ชั่วโมง เสร็จ 16 บทใน 5-7 วัน

### Day 6 — Page number + TOC + Export (1-2 ชั่วโมง)

1. **ใส่ page number** ทุกหน้า body (Canva → Position → Page numbers)
2. **อัพเดต TOC** — กรอกเลขหน้าที่ตรงกับบทในเล่มจริง
3. **เช็คลำดับหน้า** ไม่มีหน้าเว้น
4. **Export PDF Print** (Canva → Share → Download → PDF Print)
5. ตรวจ PDF บน device หลาย ๆ เครื่อง

---

## ขั้นที่ 6 — Tips & Tricks

### ใช้ Duplicate อย่างฉลาด

- ทำ Chapter Title Page 1 หน้า → Duplicate 16 รอบ → แก้เฉพาะเลข+ชื่อ
- ทำ Body Page template → Duplicate เมื่อต้องเพิ่มหน้า
- **อย่าสร้าง layout ซ้ำจากศูนย์**

### Copy-paste ไม่ loss formatting

Google Docs → Canva: copy-paste ใน **Canva Docs view** ก่อน แล้วย้ายไป design
หรือ: copy ใน Word → Save as .txt → Paste ไม่มี format → apply style เอง

### Callout box สำหรับ tips

สร้าง element group (background + border + padding) → Save as Brand Template

### Header / Footer ซ้ำทุกหน้า

Canva Pro: ใช้ **"Set as template" → Apply to all pages**

### Page break ระหว่างบท

ไม่มี "page break" ใน Canva — หน้า 1 หน้า = 1 page element
วาง Chapter Title Page ใน slot ใหม่

### สี Gradient

Canva Pro → Background → Gradient → ใส่ Navy Dark / Navy Mid → มุม 135°

### Spacing ให้สวย

- อย่าให้เนื้อหาชนขอบ — เว้น margin 15mm ขั้นต่ำ
- ย่อหน้าหลัง heading: เว้น 8pt
- ย่อหน้าก่อน heading: เว้น 16pt

---

## ขั้นที่ 7 — Export & Delivery

### Export PDF

Canva → Share → Download
- **File type:** PDF Print (คุณภาพสูงสุด ไฟล์ใหญ่)
- **Color profile:** RGB (สำหรับ digital) / CMYK (สำหรับ print)
- **Crop marks:** No
- **Flatten PDF:** Yes (รวม transparency)

### เช็คไฟล์ PDF ก่อนขาย

- [ ] ขนาดไฟล์ 5-15 MB (ถ้าเกิน 20 MB compress ก่อน)
- [ ] เปิดใน Preview (Mac), Adobe Reader, Chrome — OK ทั้งหมด
- [ ] เปิดบน iPhone / Android — Thai font ไม่เพี้ยน
- [ ] Copy text ใน PDF ได้ (ไม่ใช่ภาพ)
- [ ] Link ทำงาน (ถ้ามี)

### Watermark per buyer (ทางเลือก)

ถ้าขายผ่าน Payhip:
- Payhip ใส่ watermark อัตโนมัติหลังซื้อ
- ลูกค้าคนละคน = PDF ที่มีชื่อ+email ลูกค้านั้นฝังอยู่
- ถ้าใครแชร์ไฟล์ → รู้ว่าใครเป็นคนปล่อย

Alternative: LemonInk (paid service), SendOwl, หรือ manual ใส่ footer watermark ใน Canva

---

## ขั้นที่ 8 — Common Issues & Solutions

| ปัญหา | แก้ |
|---|---|
| Font Kanit ไม่โหลด | Canva → Text → Select font → ค้นหา "Kanit" → Add to favorites |
| Text เพี้ยนหลัง paste | Paste as plain text (Cmd+Shift+V) แล้ว apply style ใหม่ |
| PDF ไฟล์ใหญ่เกิน | Canva → PDF Standard (แทน Print) / resize ภาพก่อน upload |
| Table ดูไม่ดี | สร้างใหม่ใน Canva Table element แทน copy จาก docx |
| Page break ไม่ได้อย่างใจ | เพิ่ม page ใหม่ด้วย + button ด้านขวา |
| Color ไม่ตรง brand | ใช้ Brand Kit colors เท่านั้น (lock ไว้) |

---

## 📋 Summary checklist

- [ ] Canva Pro subscribed
- [ ] A5 document created
- [ ] Brand Kit set (colors + fonts)
- [ ] Master pages created (6 แบบ)
- [ ] Text styles saved
- [ ] Cover page ใช้ `book-cover.png`
- [ ] TOC page (ใส่เลขหน้าภายหลัง)
- [ ] Part dividers × 3
- [ ] Chapter title pages × 16
- [ ] Body content แต่ละบท
- [ ] Page numbers ทุกหน้า body
- [ ] TOC อัพเดทเลขหน้าจริง
- [ ] Export PDF Print
- [ ] Test เปิดบน device หลาย ๆ เครื่อง

---

## 🎯 ถ้าคุณไม่มีเวลา

จ้าง Freelance Fastwork
- keyword: "จัด layout ebook", "ออกแบบ e-book"
- ราคา 2,000-5,000 บาท สำหรับ 180 หน้า
- ส่ง docx + cover + brand guidelines ให้เขา
- เสร็จใน 3-5 วัน

ระวัง: Freelance บางคนใช้ template template ต้องขอดู portfolio ที่ทำแล้วก่อน

---

*คู่มือนี้อิงจากการเป็น ebook ระดับ Gumroad / Mebmarket ขาย 349 บาท ถ้าตั้งใจทำให้ premium กว่า (ขาย 990+) ลองดู design reference จาก Shopify ebooks, Canva feature templates "Magazine" แทน*
