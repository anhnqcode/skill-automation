# QA Automation Checklist
### [Mã dự án] — [Tên dự án / Module]

---

## Quan hệ với file Manual

File này là **tài liệu song song** với `Testcase_Template.md` — không thay thế, không gộp chung.

| File | Đối tượng | Mục đích |
|---|---|---|
| `Testcase_Template.md` | QA Tester | Hướng dẫn test tay, ghi kết quả P/F, báo cáo lên PM |
| `Automation_Checklist.md` (file này) | QA Engineer / SDET / Dev | Hướng dẫn viết và tổ chức test script automation |
| `QA-Auction-Automation-Checklist.md` | QA Engineer / SDET / Dev | Tầng 3 riêng cho dự án đấu giá: kịch bản, ngưỡng và dữ liệu test đặc thù. Dùng cùng file này |

**Cầu nối giữa 2 file:** Cột `Automation Status` và `Automation Link` trong bảng mẫu của file manual (Mục 24) — dùng để track case manual nào đã được automate, ở file code nào, tầng nào.

**Giá trị cột Automation Layer** trong file `.auto.md` giữ đúng danh sách ở CLAUDE.md: `E2E`, `API`, `Security`, `Performance`, `Visual`, `Manual only`, hoặc ghép hai giá trị (ví dụ `API + E2E`). Các kỹ thuật mới ở Nhóm 11–15 (điều khiển thời gian, realtime, đồng thời…) **không phải layer mới**: chúng chạy ở layer `API`, `E2E` hoặc `Performance`, ghi kỹ thuật dùng ở Phần 3 của `.auto.md`.

---

## Nguyên tắc quyết định case nào nên automate

Không phải mọi Manual TC đều nên automate. Dùng bảng dưới để quyết định:

| Loại case | Nên Automate? | Lý do |
|---|---|---|
| Happy path luồng chính (Thêm mới, Sửa, Xóa) | ✅ E2E (Nhóm 2) | Chạy hồi quy mỗi release |
| Validate field (để trống, biên, ký tự đặc biệt) | ✅ API test (Nhóm 3) | Nhanh hơn E2E, ổn định hơn |
| Security (SQLi, XSS, Auth bypass) | ✅ Security automation (Nhóm 7) | Không thể test tay đủ |
| Performance/Load | ✅ k6/JMeter (Nhóm 6) | Không thể test tay |
| Copy/Paste, thao tác cảm quan | ❌ Manual only | Khó automate, ít giá trị |
| Visual/UX cảm quan | ❌ Manual only | Automation không nhận xét được "đẹp" |
| Exploratory testing | ❌ Manual only | Bản chất là không có script cố định |
| Concurrency (2 tab cùng sửa) | ⚠️ API test thay E2E (Nhóm 3) | E2E khó, API dễ hơn |
| Phân quyền theo vai trò | ✅ API test (Nhóm 3) | Dễ automate qua header/token |
| Luồng Bộ lọc & Tìm kiếm | ✅ E2E hoặc API | Filter đơn giản → API; kết hợp nhiều điều kiện → E2E |
| Post-action behavior (thông báo, cập nhật danh sách) | ✅ E2E (Nhóm 2) | Cần UI để verify |
| Lưu trữ dữ liệu (F5, tải lại, nhất quán giữa màn hình) | ✅ API + E2E | API verify DB, E2E verify UI |
| Visual regression (thay đổi pixel ngoài ý muốn) | ✅ Visual Regression (Nhóm 10) | Phát hiện thay đổi CSS không chủ đích — khác với "cảm quan đẹp/xấu" ở dòng trên |
| State Transition — thứ tự thao tác ngược (B → A) | ✅ API (Nhóm 3) | Dễ gọi API theo thứ tự tùy ý, không cần UI |
| State Transition — trạng thái bị đổi từ module khác | ✅ API + E2E | API verify logic backend, E2E verify UI phản ánh đúng |
| Cross-module — dữ liệu chảy qua nhiều portal | ✅ E2E nhiều vai trò (Nhóm 2.10) | Cần verify UI ở nhiều portal trong cùng một test |
| Cross-module — dữ liệu tiền đề, xóa kéo theo, tham chiếu gãy | ✅ API | Setup và verify nhanh, kiểm ràng buộc trực tiếp |
| Cross-module — mỗi vai trò thấy tập trường khác nhau | ✅ API + E2E | API verify field trả về, E2E verify UI không lộ field bị ẩn |
| Cross-module — chuỗi thông báo xuyên portal | ✅ E2E + bắt email (Nhóm 14) | Cần verify thông báo ở từng portal và từng kênh |
| Time-based — kích hoạt, tự đóng theo lịch | ✅ API + điều khiển thời gian (Nhóm 11) | Không chờ thời gian thật |
| Time-based — gia hạn, race condition tại mốc | ✅ API + đồng thời (Nhóm 11, 13) | Cần gửi request đúng mili giây |
| Time-based — đồng hồ đếm ngược, hiển thị realtime | ✅ E2E + đồng hồ giả (Nhóm 11.3) | Cần verify UI |
| Realtime — sự kiện tới đủ, đúng thứ tự, đúng độ trễ | ✅ API với client WebSocket (Nhóm 12) | Không cần UI, đo được độ trễ chính xác |
| Concurrency — tranh chấp, double-submit, idempotency | ✅ API (Nhóm 13) | Chỉ tầng API bắn được request song song có kiểm soát |
| Import hàng loạt — validate dữ liệu trong file, kết quả từng phần | ✅ API | Upload file mẫu cố định qua API |
| Rollback / Undo, rollback khi giao dịch lỗi giữa chừng | ✅ API | Mô phỏng lỗi giữa chừng có kiểm soát |
| Nội dung email, file PDF/Excel/DOCX sinh ra | ✅ API + công cụ đọc file (Nhóm 14) | So nội dung thật, không chỉ kiểm "có file" |
| Ký số bằng token USB, nhập PIN thật | ❌ Manual only | Phụ thuộc phần cứng. Phần logic trước và sau bước ký vẫn automate được bằng dịch vụ ký giả (Nhóm 14.4) |
| App mobile native: tắt nền, cuộc gọi đến, push | ⚠️ E2E mobile (Nhóm 2.11) | Cần thiết bị hoặc emulator, chạy ít hơn web |

> **Phân biệt "Visual/UX cảm quan" và "Visual regression":** Cảm quan đẹp/xấu, layout có hợp lý không → Manual only, automation không nhận xét được. Pixel thay đổi so với baseline sau release → Visual regression automation phát hiện được.

---

## Mục lục

1. [Nhóm 0: Nguyên tắc chung & CI/CD Integration](#nhóm-0)
2. [Nhóm 1: Smoke Test & Sanity Test](#nhóm-1)
3. [Nhóm 2: UI Automation / E2E Testing](#nhóm-2)
4. [Nhóm 3: API Testing](#nhóm-3)
5. [Nhóm 4: Integration Testing](#nhóm-4)
6. [Nhóm 5: Database / Data Integrity Testing](#nhóm-5)
7. [Nhóm 6: Performance Testing](#nhóm-6)
8. [Nhóm 7: Security Testing](#nhóm-7)
9. [Nhóm 8: Contract Testing](#nhóm-8)
10. [Nhóm 9: Accessibility Automation (a11y)](#nhóm-9)
11. [Nhóm 10: Visual Regression Testing](#nhóm-10)
12. [Nhóm 11: Điều khiển thời gian và tác vụ theo lịch](#nhóm-11)
13. [Nhóm 12: Realtime / WebSocket](#nhóm-12)
14. [Nhóm 13: Đồng thời, idempotency và bất biến nghiệp vụ](#nhóm-13)
15. [Nhóm 14: Kiểm đầu ra ngoài giao diện](#nhóm-14)
16. [Nhóm 15: Dữ liệu test, độ ổn định và chỉ số automation](#nhóm-15)

---

## Nhóm 0: Nguyên tắc chung & CI/CD Integration

### 0.1. Phân tầng automation (Test Pyramid)

Tuân theo nguyên tắc phân tầng để đảm bảo bộ test nhanh, ổn định, và có giá trị cao:

```
           /\
          /E2E\          ← Ít nhất (~5-10%), chậm nhất, test luồng người dùng thực
         /------\
        /  API   \       ← Tầng giữa (~20-30%), validate contract + server logic
       /----------\
      / Unit /      \    ← Nhiều nhất (~60-70%), nhanh nhất, test logic đơn lẻ
     / Integration   \
    /------------------\
```

- **Unit/Integration test** — chiếm 60-70%: test logic nghiệp vụ, tính toán, transform dữ liệu ở mức hàm/module, không qua network
- **API test** — chiếm 20-30%: validate input/output của từng endpoint, không qua UI
- **E2E test** — chiếm 5-10%: chỉ các luồng nghiệp vụ quan trọng nhất, chạy qua UI thực

> **Quy tắc vàng:** Không viết E2E cho những gì API test đã cover — tránh bộ test chậm, dễ vỡ (brittle), và trùng lặp.

### 0.2. Quy tắc viết automation test

- Mỗi test phải **độc lập**: không phụ thuộc thứ tự chạy, không phụ thuộc dữ liệu test khác để lại
- Mỗi test chỉ kiểm tra **một mục tiêu** (giống quy tắc ở manual test)
- Tên test phải mô tả rõ hành vi: `should return 400 when email is missing` — không đặt tên `test1`, `case2`
- Không dùng `sleep(N)` cố định — dùng explicit wait hoặc polling theo điều kiện cụ thể
- Không hardcode URL, credential, environment-specific value — đưa vào config file hoặc environment variable
- Mỗi test tự **setup data** trước khi chạy và **cleanup** sau khi chạy, không để lại "rác" trong DB test
- Mỗi test automation phải có thể **truy vết ngược** về Manual TC tương ứng qua tag/comment (ví dụ `// @TC-DMTS-020`)

### 0.3. CI/CD Pipeline Integration

Phân chia rõ nhóm test nào chạy ở giai đoạn nào trong pipeline:

| Giai đoạn | Nhóm test chạy | Trigger | Thời gian mục tiêu |
|---|---|---|---|
| **Pre-commit** | Unit test | Mỗi lần commit (git hook) | < 30 giây |
| **Pull Request** | Unit + Integration + API + Smoke test + Contract test | Mỗi PR tạo/update | < 10 phút |
| **Merge to main/staging** | Unit + Integration + API + E2E (luồng chính) + Security scan | Sau khi merge | < 30 phút |
| **Nightly** | Toàn bộ E2E + Performance + Soak test + Visual Regression + a11y scan | Hàng đêm lúc ít traffic | Không giới hạn cứng |
| **Pre-production** | Smoke test + Sanity test | Trước mỗi deployment lên production | < 5 phút |

> **Quy tắc fail pipeline:** Test ở giai đoạn nào fail thì block deployment tương ứng — không merge PR khi API test fail, không deploy production khi Smoke test fail.

### 0.4. Ngưỡng SLA tham chiếu mẫu

> Đây là ngưỡng **khởi điểm tham chiếu** — bắt buộc phải điều chỉnh theo NFR (Non-Functional Requirements) đã thống nhất với stakeholder của từng dự án cụ thể. Dùng **p95** làm ngưỡng chính thức, không dùng average (average bị méo bởi outlier).
>
> **Dự án đấu giá:** chức năng nào đã có NFR riêng (phòng đấu, realtime, thông báo kết quả) thì dùng ngưỡng ở `QA-Auction-Automation-Checklist.md` Mục G.0, bảng dưới chỉ áp cho phần còn lại.

| Loại endpoint | p50 | p95 | p99 | Error rate tối đa |
|---|---|---|---|---|
| GET danh sách (< 100 bản ghi) | < 100ms | < 300ms | < 500ms | < 0.1% |
| GET danh sách (phân trang lớn, > 1000 bản ghi) | < 200ms | < 500ms | < 1s | < 0.1% |
| GET chi tiết 1 bản ghi | < 50ms | < 200ms | < 400ms | < 0.1% |
| POST tạo mới | < 200ms | < 500ms | < 1s | < 0.1% |
| PUT/PATCH cập nhật | < 200ms | < 500ms | < 1s | < 0.1% |
| DELETE | < 100ms | < 300ms | < 500ms | < 0.1% |
| Search/Filter phức tạp (nhiều điều kiện) | < 300ms | < 800ms | < 2s | < 0.5% |
| Export file (< 1000 bản ghi) | < 2s | < 5s | < 10s | < 1% |
| Report / Dashboard tổng hợp nặng | < 3s | < 8s | < 15s | < 1% |

---

## Nhóm 1: Smoke Test & Sanity Test

> Bộ test tối thiểu chạy sau mỗi deployment để xác nhận hệ thống vẫn "sống" và các luồng cốt lõi không bị vỡ. **Phải chạy xong trong < 5 phút.** Công cụ: bất kỳ framework nào — Playwright, pytest, Newman.

### 1.1. Health check & Connectivity
- Endpoint health check (`/health`, `/ping`, hoặc tương đương) của hệ thống trả về 200 OK
- Kết nối database thành công — không timeout, không lỗi connection pool
- Kết nối các service phụ thuộc quan trọng (cache, message queue, external service thiết yếu) còn hoạt động

### 1.2. Authentication Smoke
- Đăng nhập với tài khoản test hợp lệ → nhận được token/session hợp lệ trong response
- Token/session nhận được có thể dùng để gọi API có bảo vệ thành công (không bị 401)

### 1.3. Core CRUD Smoke
- **Create**: POST tạo 1 bản ghi với dữ liệu tối thiểu hợp lệ → response 200/201, bản ghi có ID
- **Read**: GET bản ghi vừa tạo theo ID → response 200, đúng dữ liệu
- **Update**: PUT/PATCH cập nhật bản ghi → response 200, dữ liệu thay đổi
- **Delete**: DELETE bản ghi → response 200/204, GET lại trả 404
- Toàn bộ 4 bước hoàn thành trong < 10 giây

### 1.4. Sanity Check sau Hotfix / Patch
- Các luồng bị ảnh hưởng trực tiếp bởi thay đổi vừa deploy vẫn hoạt động đúng
- Các luồng kề cận (dùng chung code/data/service) không bị ảnh hưởng ngoài ý muốn
- Sanity test được cập nhật mỗi khi có hotfix mới để phản ánh đúng phạm vi rủi ro của thay đổi đó

---

## Nhóm 2: UI Automation / End-to-End Testing (E2E)

> Tự động hóa các luồng người dùng quan trọng qua giao diện thực. Công cụ khuyến nghị: **Playwright** (hỗ trợ đa browser, có built-in wait, API request interception). Thay thế: Cypress, Selenium.

### 2.1. Cấu trúc 1 Test Case E2E chuẩn (AACA)

Mỗi test E2E phải có đủ 4 phần theo pattern **Arrange → Act → Assert → Cleanup**:

```javascript
test('TC-DMTS-020: Tạo mới danh mục với Tên hợp lệ', async ({ page }) => {

  // ARRANGE — Setup dữ liệu qua API (không qua UI, nhanh và ổn định hơn)
  const token = await loginAPI('admin', 'password');
  const parentCategory = await createCategoryAPI(token, { name: 'Danh mục cha test' });
  await page.goto('/categories');

  // ACT — Thực hiện đúng 1 hành động người dùng
  await page.getByTestId('btn-add-category').click();
  await page.getByTestId('input-category-name').fill('Xe máy');
  await page.getByTestId('select-parent').selectOption(parentCategory.id);
  await page.getByTestId('btn-save').click();

  // ASSERT — Kiểm tra UI + kiểm tra dữ liệu thực sự được lưu
  await expect(page.getByTestId('toast-success')).toContainText('Thêm mới thành công');
  await expect(page.getByText('Xe máy')).toBeVisible();
  // Xác nhận dữ liệu thực sự lưu vào DB qua API — không chỉ tin vào UI
  const created = await getCategoryByNameAPI(token, 'Xe máy');
  expect(created.name).toBe('Xe máy');
  expect(created.parentId).toBe(parentCategory.id);

  // CLEANUP — Dọn sạch dữ liệu test
  await deleteCategoryAPI(token, created.id);
  await deleteCategoryAPI(token, parentCategory.id);
});
```

### 2.2. Chiến lược Selector (Selector Strategy)

Ưu tiên theo thứ tự — dùng loại cao hơn khi có thể:

| Thứ tự ưu tiên | Loại selector | Ví dụ | Lý do |
|---|---|---|---|
| 1 (tốt nhất) | `data-testid` | `[data-testid="btn-save"]` | Ổn định nhất, không bị ảnh hưởng bởi thay đổi UI/CSS |
| 2 | ARIA role + label | `getByRole('button', { name: 'Lưu' })` | Semantic, cũng hỗ trợ a11y test |
| 3 | Text content | `getByText('Lưu')` | Dễ đọc nhưng dễ vỡ khi đổi ngôn ngữ/text |
| 4 | CSS class | `.btn-primary` | Chỉ dùng khi không còn lựa chọn khác |
| ❌ Tránh | XPath phức tạp | `//div[3]/ul/li[2]/a` | Vỡ khi thay đổi cấu trúc DOM |
| ❌ Tránh | Generated class | `.css-a1b2c3` | Thay đổi mỗi lần build |
| ❌ Tránh | Index-based | `li:nth-child(3)` | Vỡ khi thay đổi thứ tự |

> **Phối hợp với Dev team:** Đảm bảo mọi interactive element quan trọng (button, input, form, toast, modal) đều có `data-testid` từ giai đoạn development — không phải thêm vào sau khi viết test.

### 2.3. Luồng Thêm mới (Create E2E)
- **Arrange:** Tạo dữ liệu phụ cần thiết qua API (dữ liệu cha, lookup data...)
- **Act:** Mở form → điền từng field với test data đã định nghĩa → bấm Lưu
- **Assert UI:** Thông báo thành công hiển thị đúng nội dung và vị trí; bản ghi xuất hiện trong danh sách không cần F5; vị trí đúng theo sort hiện tại
- **Assert Data:** Gọi GET API để xác nhận dữ liệu thực sự được lưu đúng (đúng giá trị, đúng quan hệ)
- **Cleanup:** Xóa bản ghi test qua API

### 2.4. Luồng Chỉnh sửa (Update E2E)
- **Arrange:** Tạo bản ghi test với giá trị ban đầu qua API
- **Act:** Mở bản ghi → sửa các field cần test → bấm Lưu
- **Assert UI:** Thông báo thành công; dữ liệu mới hiển thị đúng trên form và trong danh sách
- **Assert Data:** Gọi GET API để xác nhận dữ liệu thực sự được cập nhật; dữ liệu cũ không còn
- **Cleanup:** Xóa bản ghi test qua API

### 2.5. Luồng Xóa (Delete E2E)
- **Arrange:** Tạo bản ghi test qua API
- **Act:** Chọn bản ghi → bấm Xóa → xác nhận trong popup
- **Assert UI:** Thông báo thành công; bản ghi biến khỏi danh sách
- **Assert Data:** GET API với ID vừa xóa → nhận 404 (xác nhận thực sự xóa, không chỉ ẩn trên UI)
- **Cleanup:** Không cần (đã xóa)

### 2.6. Luồng Bộ lọc & Tìm kiếm (Search/Filter E2E)
- **Arrange:** Tạo ít nhất 5 bản ghi test với dữ liệu đa dạng qua API để có đủ tập test
- Áp dụng 1 điều kiện lọc → assert đúng số lượng kết quả, đúng bản ghi hiển thị
- Kết hợp 2-3 điều kiện lọc → assert kết quả đúng theo AND logic (xem thêm Manual Mục 4.2)
- Nhập từ khóa tìm kiếm → assert kết quả đúng, không trả thừa/thiếu
- Reset bộ lọc → assert danh sách trở về đúng trạng thái ban đầu
- **Cleanup:** Xóa toàn bộ bản ghi test qua API

### 2.7. Luồng Phân quyền (Auth E2E)
- Đăng nhập vai trò không có quyền xem/sửa → assert không thấy nút/menu bị ẩn đúng theo thiết kế
- Truy cập trực tiếp URL yêu cầu quyền cao hơn → assert bị redirect hoặc thông báo lỗi đúng
- Không hardcode credential — đọc từ environment variable hoặc test config file

### 2.8. Post-action Behavior E2E
- Sau Thêm mới thành công → toast notification hiển thị đúng, tự ẩn sau đúng thời gian, không còn hiển thị sau khi đã ẩn
- Sau Chỉnh sửa thành công → form đóng/giữ lại theo đúng thiết kế, danh sách cập nhật không cần F5
- Sau Xóa thành công → bản ghi biến khỏi danh sách, tổng số bản ghi trong pagination cập nhật đúng

### 2.9. Tổ chức code theo Page Object Model (POM)

```
tests/
├── e2e/
│   ├── pages/                    ← Page Object classes
│   │   ├── CategoryListPage.ts   ← Locator + action của màn Danh sách
│   │   ├── CategoryFormPage.ts   ← Locator + action của form Thêm mới/Chỉnh sửa
│   │   └── BasePage.ts           ← Các method dùng chung
│   ├── fixtures/                 ← Test data cố định
│   │   └── category.fixture.ts
│   ├── helpers/                  ← API helpers cho setup/cleanup
│   │   └── category.api.ts
│   └── specs/                    ← Test files
│       └── category.spec.ts
```

- Test file chỉ gọi method của POM, **không chứa locator trực tiếp**
- Khi UI thay đổi locator → chỉ sửa ở POM, mọi test dùng POM đó tự cập nhật
- Không duplicate logic giữa các test — đưa vào helper/fixture để tái sử dụng

### 2.10. E2E nhiều vai trò trong cùng một test (Multi-actor)

> Dùng khi một nghiệp vụ cần nhiều người ở nhiều portal cùng thao tác, ví dụ tổ chức tạo và công bố, khách đăng ký, hai khách cùng ở phòng đấu, chủ tài sản theo dõi. Playwright mở mỗi vai trò bằng một **browser context** riêng, có cookie và phiên đăng nhập riêng.

- Mỗi vai trò một context, đăng nhập bằng `storageState` đã chuẩn bị sẵn qua API, không đăng nhập qua UI trong từng test
- Đặt tên biến theo vai trò (`partnerPage`, `customerA`, `customerB`, `holderPage`) để đọc test là biết ai đang làm gì
- Assert ở **từng portal** sau mỗi bước quan trọng, giống quy tắc viết kết quả mong muốn của case cross-module ở `Testcase_Template.md` Mục 27.8
- Chờ theo điều kiện (giá mới xuất hiện, trạng thái đổi), không chờ cố định số giây
- Giới hạn số context trong một test (khuyến nghị không quá 5) để test không quá chậm và khó đọc

### 2.11. E2E trên app mobile native

> Áp dụng khi dự án có app mobile riêng, không chỉ là web responsive. Công cụ: **Maestro** (dễ viết, ổn định), **Appium** (đa nền tảng, linh hoạt), **Detox** (React Native).

- Chỉ automate luồng chính và các tình huống đặc thù mobile mà web không có: tắt app xuống nền rồi mở lại, khóa màn hình, mất mạng rồi có mạng, mở từ thông báo đẩy, mở từ deep link
- Chạy trên emulator ở pipeline Nightly, chạy trên thiết bị thật trước mỗi lần phát hành app
- Phần nghiệp vụ dùng chung API với web thì không viết lại ở mobile, vì đã có API test phủ

---

## Nhóm 3: API Testing

> Kiểm tra trực tiếp các API endpoint. Công cụ khuyến nghị: **pytest + httpx** (Python) hoặc **Jest + supertest** (Node.js) hoặc **Postman/Newman** (no-code). Chạy nhanh hơn E2E 10-50 lần.

### 3.1. Functional API Testing
- Request hợp lệ → status code đúng (200/201), cấu trúc JSON đúng schema, dữ liệu đúng giá trị
- Request thiếu trường bắt buộc → 400/422 kèm error body mô tả rõ **trường nào sai, lỗi gì**
- Request sai định dạng (email sai format, số âm khi không cho phép) → đúng status code lỗi
- Request xóa/sửa bản ghi không tồn tại → 404 với error body phù hợp
- Request tạo bản ghi với giá trị unique đã tồn tại → 409 Conflict

### 3.2. Server-side Validation (bypass UI)
- Gửi trực tiếp qua API (curl/script) với dữ liệu vi phạm validate mà UI đã chặn → **server vẫn phải validate và từ chối** — xác nhận validate không chỉ ở client
- Dữ liệu vượt max-length, max-value → server từ chối, không truncate âm thầm
- Kiểu dữ liệu sai (string thay vì number, array thay vì string, null cho required field) → server trả lỗi rõ ràng
- Body rỗng hoàn toàn `{}` hoặc `null` → server không crash, trả 400 rõ ràng

### 3.3. Authentication & Authorization API
- Request không có token → 401, không trả về bất kỳ dữ liệu nào
- Token hết hạn → 401, không tự gia hạn
- Token hợp lệ nhưng không đủ quyền → 403 Forbidden
- Token giả mạo hoặc bị thay đổi 1 ký tự → bị từ chối, không trả dữ liệu

### 3.4. Response Contract
- Tất cả field trong response có mặt đầy đủ, đúng kiểu (string/number/boolean/array/null)
- Field nullable: không trả `undefined`, chỉ trả `null` hoặc bỏ qua field (nhất quán)
- **Field nhạy cảm không xuất hiện trong response:** password hash, private key, secret, internal token — với bất kỳ vai trò nào
- Pagination: `total`, `page`, `page_size`, `data` array — giá trị đúng với thực tế trong DB

### 3.5. Edge Case API
- Concurrent request tạo cùng 1 bản ghi unique → chỉ 1 bản ghi được tạo, không duplicate
- Payload quá lớn (> limit cho phép) → 413 Payload Too Large
- Query string/param encoding đặc biệt (ký tự UTF-8, URL-encoded) → xử lý đúng
- Phân trang vượt tổng số trang → trả `data: []`, không báo lỗi

### 3.6. Cấu trúc 1 API Test chuẩn

```python
# Python + pytest + httpx — ví dụ
# @TC-DMTS-020
def test_create_category_with_valid_name(api_client, auth_token, cleanup):
    # Arrange
    payload = {"name": "Xe máy", "code": "XM001"}
    
    # Act
    response = api_client.post(
        "/api/v1/categories",
        json=payload,
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    
    # Assert
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Xe máy"
    assert body["code"] == "XM001"
    assert "id" in body
    assert "password" not in body          # Sensitive field không được lộ
    assert "createdAt" in body
    
    # Cleanup (qua fixture)
    cleanup.add_category(body["id"])
```

---

## Nhóm 4: Integration Testing

> Kiểm tra sự phối hợp đúng giữa các module/service — ở mức code/service, không qua UI. Khác với E2E (toàn stack qua UI) và API test (1 endpoint đơn lẻ). Công cụ: **pytest**, **Jest**, **TestContainers** (spin up DB/service thực trong Docker cho test).

### 4.1. Tích hợp giữa các Module nội bộ
- Module A gọi Module B: dữ liệu đầu ra của A được B xử lý đúng theo interface đã định nghĩa
- Thay đổi internal của A (không đổi interface) → B không bị ảnh hưởng
- Thay đổi interface của A mà chưa update B → integration test fail và báo sớm

### 4.2. Tích hợp với Cơ sở dữ liệu
- Transaction: nhiều thao tác trong cùng 1 transaction — commit khi tất cả thành công, rollback toàn bộ khi 1 bước thất bại
- Ràng buộc DB (FK, unique, not null) hoạt động đúng khi vi phạm từ code — không chỉ dựa validate ở application layer
- Query phức tạp (join nhiều bảng, aggregation, subquery) trả đúng kết quả trên bộ dữ liệu test đã kiểm soát

### 4.3. Tích hợp với Message Queue (nếu áp dụng)
- Publish message → consumer nhận đúng message và xử lý đúng logic
- Consumer xử lý thất bại → message được retry hoặc chuyển vào dead letter queue theo đúng cấu hình
- Xử lý duplicate message → idempotent: kết quả giống nhau dù xử lý 2 lần cùng message

### 4.4. Tích hợp với External Service (nếu áp dụng)
- Dùng **mock/stub** thay thế external service để test không phụ thuộc vào service ngoài
- Mock external service trả lỗi (500, timeout, network error) → hệ thống xử lý đúng theo fallback
- Mock external service trả dữ liệu sai format → hệ thống không crash, log lỗi đúng cách

---

## Nhóm 5: Database / Data Integrity Testing

> Kiểm tra tính toàn vẹn dữ liệu tại tầng DB — tách biệt với application logic. Công cụ: **pytest + SQLAlchemy**, **dbt test**, **pgTAP** (PostgreSQL).

### 5.1. Ràng buộc dữ liệu (DB Constraints)
- **Unique constraint:** Insert bản ghi trùng giá trị unique trực tiếp vào DB → bị reject với constraint violation error
- **Not null constraint:** Insert bản ghi với null cho cột required → bị reject
- **Foreign key constraint:** Insert bản ghi con với FK trỏ đến ID không tồn tại → bị reject
- **Check constraint** (nếu có): Insert giá trị vi phạm check rule → bị reject

### 5.2. Cascade và Referential Integrity
- Xóa bản ghi cha có bản ghi con → hành vi đúng theo thiết kế: cascade delete, restrict, hoặc set null
- Sau các thao tác xóa: **không tồn tại dữ liệu orphan** (bản ghi con có FK trỏ đến ID đã bị xóa) — kiểm tra bằng query tìm FK không hợp lệ
- Cập nhật PK (nếu được phép) → cascade update FK ở bảng con đúng

### 5.3. Toàn vẹn sau Database Migration
- Sau mỗi migration: tổng số bản ghi không thay đổi ngoài ý muốn (so sánh count trước/sau)
- Dữ liệu cũ vẫn readable và đúng format sau migrate: không bị truncate, không lỗi encoding
- Index vẫn hoạt động đúng sau migration: query dùng index column vẫn trả kết quả đúng

### 5.4. Transaction & Concurrency ở tầng DB
- Concurrent update cùng bản ghi: locking mechanism hoạt động đúng, không xảy ra **lost update** (bản cập nhật sau ghi đè lên bản cập nhật trước mà không biết)
- Deadlock: hệ thống có cơ chế phát hiện và xử lý, không để transaction treo vô thời hạn
- Long-running transaction: không chiếm lock quá lâu gây block các transaction khác

---

## Nhóm 6: Performance Testing

> Đo lường thời gian phản hồi và hành vi dưới tải. Công cụ khuyến nghị: **k6** (script-based, CI-friendly, report đẹp). Thay thế: JMeter, Locust, Artillery.

### 6.1. Baseline Performance (Single User)
- Đo p50/p95/p99 của từng API endpoint quan trọng ở điều kiện 1 user
- So sánh với ngưỡng SLA tại Mục 0.4 — **fail test tự động nếu vượt ngưỡng**
- Đo riêng các endpoint nặng (search phức tạp, export, report) với ngưỡng riêng phù hợp

### 6.2. Load Testing (Multi User)
- Mô phỏng **normal load** → tất cả SLA metric vẫn đạt
- Mô phỏng **peak load** (1.5×–2× normal) → đo degradation, xác nhận trong ngưỡng chấp nhận
- Mô phỏng **traffic pattern thực tế**: đọc nhiều hơn ghi (ví dụ 70% GET / 20% POST / 10% PUT+DELETE) — không hammer 1 loại request
- Dùng `ramping VU` (tăng dần user) thay vì đẩy full load ngay lập tức — phản ánh đúng hành vi thực

```javascript
// k6 example — load test với ramping VU
export const options = {
  stages: [
    { duration: '2m', target: 50 },   // Ramp up lên 50 users trong 2 phút
    { duration: '5m', target: 50 },   // Giữ 50 users trong 5 phút
    { duration: '2m', target: 0 },    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // p95 phải < 500ms
    http_req_failed: ['rate<0.001'],   // Error rate < 0.1%
  },
};
```

### 6.3. Stress Testing
- Tăng dần tải cho đến khi error rate > 1% hoặc p95 > ngưỡng × 3 → ghi lại **breaking point**
- Sau khi giảm tải → hệ thống phục hồi hoàn toàn: p95 về baseline, error rate về 0
- Hệ thống thất bại **gracefully**: trả thông báo lỗi rõ ràng, không crash toàn bộ service

### 6.4. Soak Testing (Độ bền)
- Chạy normal load liên tục **2–4 giờ** (hoặc theo yêu cầu dự án)
- Monitor trong suốt thời gian chạy:
  - Memory: không tăng liên tục không giới hạn (memory leak)
  - CPU: ổn định, không spike liên tục
  - DB connections: không tăng dần (connection leak)
  - Response time: p95 ở cuối soak không chênh quá **20%** so với lúc đầu

### 6.5. Spike Testing
- Tăng đột ngột từ baseline lên peak trong < 30 giây → hệ thống không crash, xử lý được hoặc queue request đúng cách
- Sau spike kết thúc → hệ thống phục hồi trong thời gian đã định nghĩa (ví dụ < 60 giây)

---

## Nhóm 7: Security Testing (Automation)

> Tự động phát hiện lỗ hổng bảo mật. Công cụ: **OWASP ZAP** (scan tự động), **Semgrep** (static analysis), **trivy** (dependency/image scan), **OWASP Dependency-Check**.

### 7.1. Injection Attacks
- **SQL Injection:** Tự động gửi payload SQLi phổ biến (`' OR '1'='1`, `'; DROP TABLE`, UNION-based, time-based blind) vào toàn bộ input field, query param, path param, header → không endpoint nào trả dữ liệu DB nhạy cảm hoặc SQL error message
- **XSS (Reflected & Stored):** Gửi payload XSS (`<script>alert(1)</script>`, event handler, `javascript:` URI) vào toàn bộ input → payload không được thực thi khi render lại
- **Command Injection:** Ở endpoint liên quan đến file (upload, download, convert) → không thực thi lệnh OS

### 7.2. CSRF Protection
- Endpoint thay đổi trạng thái (POST/PUT/DELETE) yêu cầu CSRF token hoặc dùng SameSite cookie + Origin validation
- Request **không có CSRF token** hoặc token sai → bị reject với 403
- Request từ **origin không được phép** → bị reject theo CORS policy đã cấu hình, không cho phép cross-origin write

### 7.3. Rate Limiting
- Gửi request lặp lại nhanh đến endpoint login → bị rate limit sau N lần thất bại liên tiếp với **429 Too Many Requests**
- Response 429 có header `Retry-After` hoặc thông báo rõ thời gian phải chờ
- Gửi hàng loạt request đến endpoint thông thường vượt limit → bị throttle đúng cách
- Sau thời gian cooldown → request được chấp nhận trở lại bình thường

### 7.4. Authentication & Authorization
- **IDOR** (Insecure Direct Object Reference): Thay đổi ID bản ghi trong URL/body để truy cập bản ghi của user khác → bị từ chối 403/404, không trả dữ liệu
- **Privilege Escalation:** User vai trò thấp gọi trực tiếp API endpoint của vai trò cao → bị từ chối 403
- **JWT Misconfiguration:** Thử `alg: none`, thử thay đổi payload mà không ký lại, thử dùng secret yếu → tất cả bị từ chối

### 7.5. Sensitive Data Exposure
- Response không chứa: password hash, private key, internal config, full stack trace (ở production)
- Header response không tiết lộ thông tin nhạy cảm: `X-Powered-By`, `Server` version, OS info
- HTTPS được enforce: request HTTP bị redirect 301 về HTTPS, không cho downgrade

### 7.6. Dependency & Supply Chain Security
- Quét toàn bộ dependency (`npm audit`, `pip audit`, `mvn dependency-check`) → **fail build nếu có CVE mức Critical hoặc High** chưa được xử lý
- Quét Docker image layers → không có known vulnerability trong base image và các package được cài vào
- Chạy tự động trong CI/CD pipeline mỗi khi merge — không chỉ chạy theo yêu cầu

---

## Nhóm 8: Contract Testing

> Xác nhận API contract giữa các bên (FE-BE, service-service) không bị vỡ sau thay đổi — **phát hiện breaking change trước khi đến production**. Công cụ: **Pact**, **Schemathesis**, **Dredd**.

### 8.1. Consumer-Driven Contract (FE → BE)
- Frontend định nghĩa contract: field nào cần, kiểu dữ liệu, response structure
- Backend chạy Pact verification sau mỗi merge: xác nhận API hiện tại không vi phạm contract đã định nghĩa
- BE xóa field / đổi tên field / đổi kiểu mà chưa update contract → **Pact test fail ngay**, không đợi FE gặp lỗi production

### 8.2. OpenAPI Schema Validation
- Validate response của mọi endpoint theo OpenAPI/Swagger schema đã định nghĩa (Schemathesis tự động generate test case từ schema)
- Phát hiện sai lệch giữa tài liệu API và API thực tế: field thiếu, kiểu sai, nullable không khớp, enum value ngoài danh sách
- Chạy tự động mỗi khi API code thay đổi — không phải chỉ khi cập nhật tài liệu

### 8.3. Backward Compatibility
- **Additive change** (thêm field mới vào response) → consumer cũ không bị vỡ — test xác nhận điều này
- **Breaking change** (xóa/đổi tên field) → phải bump API version — contract test fail và ngăn merge cho đến khi có version mới

---

## Nhóm 9: Accessibility Automation (a11y)

> Tự động phát hiện ~30–40% vi phạm a11y có thể kiểm tra bằng máy. Phần còn lại vẫn cần test tay (screen reader, cognitive load, UX cảm nhận). Công cụ: **axe-core** (tích hợp vào Playwright/Cypress), **Lighthouse CI**, **pa11y**.

### 9.1. Axe-core Scan tích hợp E2E
- Tích hợp axe-core vào E2E test: sau khi load mỗi màn hình chính, tự động quét và **fail test nếu có vi phạm mức critical hoặc serious**
- Không có vi phạm:
  - Input field không có label liên kết (for/id hoặc aria-label)
  - Ảnh có nội dung không có alt text
  - Color contrast ratio < 4.5:1 (text thường) hoặc < 3:1 (text lớn/bold)
  - Interactive element không thể focus bằng keyboard
  - Focus indicator không hiển thị rõ

### 9.2. Lighthouse CI
- Chạy sau mỗi deployment lên staging
- Accessibility score ≥ 90 (ngưỡng tham chiếu — điều chỉnh theo yêu cầu dự án)
- **Fail pipeline nếu score giảm** so với baseline trước đó (regression detection)
- Lưu lịch sử score để theo dõi trend theo thời gian

---

## Nhóm 10: Visual Regression Testing

> Phát hiện thay đổi giao diện không mong muốn bằng so sánh ảnh chụp. Công cụ: **Percy** (cloud-based, tích hợp CI tốt), **Chromatic** (tích hợp với Storybook), **Playwright Screenshot** (self-hosted).

### 10.1. Baseline Capture & Comparison
- Chụp baseline của màn hình và component quan trọng sau lần approve đầu tiên hoặc sau mỗi release được duyệt
- Sau mỗi deploy/merge, tự động chụp lại và so sánh với baseline
- **Fail nếu diff vượt ngưỡng** (ví dụ > 0.1% số pixel khác nhau — điều chỉnh theo nhu cầu)
- Phân loại rõ:
  - Thay đổi có chủ đích → **approve baseline mới** để cập nhật reference
  - Thay đổi ngoài ý muốn → **fail build**, cần fix

### 10.2. Xử lý Dynamic Content (tránh False Positive)

Dynamic content là nguyên nhân phổ biến nhất gây false positive trong visual test — cần xử lý trước khi chụp ảnh:

- **Mask** (che vùng dynamic trước khi chụp): timestamp, ngày giờ, avatar generate ngẫu nhiên, ID tự tăng, dữ liệu real-time, loading spinner
- Dùng attribute `data-visual-test="ignore"` (hoặc tương đương của tool) để đánh dấu vùng cần che
- Dùng **mock data cố định** trong visual test (không dùng dữ liệu live) — đảm bảo ảnh baseline ổn định giữa các lần chạy
- **Disable animation/transition** trong test environment:
  ```css
  /* Thêm vào CSS khi chạy visual test */
  *, *::before, *::after {
    animation-duration: 0s !important;
    transition-duration: 0s !important;
  }
  ```
- Với animation không disable được: chờ animation kết thúc hoàn toàn trước khi chụp, dùng `waitForSelector('[data-animation-done]')`

### 10.3. Phạm vi Viewport
- Test tối thiểu trên **3 viewport**: desktop (1440×900), tablet (768×1024), mobile (375×812)
- Với module có hỗ trợ Mobile (xem Manual Mục 21): bổ sung thêm viewport theo thiết bị phổ biến của người dùng thực tế (lấy từ analytics)
- Mỗi viewport có baseline riêng — không dùng chung baseline giữa các viewport

---

## Nhóm 11: Điều khiển thời gian và tác vụ theo lịch

> Mọi chức năng có mốc thời gian (mở, đóng, gia hạn, hết hạn, chạy theo lịch) **không được automate bằng cách chờ thời gian thật**. Test sẽ chậm, và lỗi ở đúng mốc thời gian gần như không tái hiện được. Nhóm này cần dev hỗ trợ từ đầu dự án, xem 11.1.

### 11.1. Yêu cầu testability gửi dev (làm một lần, dùng cho cả dự án)

| Yêu cầu | Dùng để |
|---|---|
| Môi trường test cho phép **đặt giờ máy chủ** (time travel) hoặc tiêm đồng hồ giả vào service, chỉ bật ở môi trường test | Đưa hệ thống tới đúng mốc mà không phải chờ |
| Các thời lượng nghiệp vụ (độ dài phiên, độ dài vòng, mốc cảnh báo) **cấu hình được ở môi trường test** | Chạy cả phiên trong vài chục giây |
| Endpoint nội bộ **kích hoạt ngay** từng tác vụ theo lịch (job công bố, đóng, đối soát…), chỉ bật ở môi trường test | Không chờ cron |
| Endpoint đọc giờ máy chủ có độ chính xác mili giây | Canh request đúng mốc |

### 11.2. Kịch bản bắt buộc cho mỗi mốc thời gian

- Thao tác ở [mốc − 1 giây], [đúng mốc], [mốc + 1 giây]. Chạy lặp ít nhất 20 lần, kết quả phải giống nhau mọi lần
- Tác vụ theo lịch được kích hoạt hai lần liên tiếp: kết quả giống như chạy một lần
- Máy chủ dừng qua mốc rồi chạy lại: tác vụ được xử lý bù đúng quy tắc, không bỏ sót, không chạy hai lần
- Đổi cấu hình mốc ngay trước khi tới mốc: tác vụ chạy theo cấu hình mới

### 11.3. Đồng hồ trên giao diện

- Dùng `page.clock` của Playwright (hoặc tương đương) để tua đồng hồ trình duyệt, kiểm đếm ngược, nút tự khóa khi về 0, popup cảnh báo hiện đúng mốc
- Đặt giờ máy khách lệch 5 phút so với máy chủ: đồng hồ hiển thị vẫn theo giờ máy chủ

---

## Nhóm 12: Realtime / WebSocket

> Kiểm kênh đẩy dữ liệu tức thời ở tầng giao thức, không qua UI. Công cụ: client WebSocket trong test (thư viện `ws` của Node, `websockets` của Python), **k6** module `k6/ws` hoặc `k6/experimental/websockets` cho tải.

- Mở nhiều client cùng đăng ký một kênh, phát một sự kiện: **mọi** client nhận được, đúng nội dung, trong ngưỡng độ trễ
- Đo độ trễ từ lúc máy chủ chấp nhận thao tác tới lúc client nhận sự kiện. Đo bằng thời gian máy chủ ghi trong sự kiện, không đo bằng giờ máy test
- Nhiều sự kiện liên tiếp: client nhận đúng thứ tự, không thiếu, không trùng
- Ngắt kết nối giữa chừng rồi kết nối lại: client đồng bộ lại đủ dữ liệu đã lỡ
- Client đăng ký kênh **không thuộc quyền** của mình (phòng khác, tổ chức khác): bị từ chối, không nhận sự kiện
- Nội dung sự kiện gửi xuống không chứa trường mà vai trò đó không được thấy

---

## Nhóm 13: Đồng thời, idempotency và bất biến nghiệp vụ

### 13.1. Bắn request đồng thời có kiểm soát

- Dùng **barrier**: chuẩn bị sẵn N request, giữ lại, rồi thả cùng lúc (`Promise.all` sau một mốc chung, `asyncio.gather`, hoặc k6 với nhiều VU bắt đầu cùng mốc)
- Mỗi kịch bản đồng thời chạy lặp **ít nhất 50 lần**. Lỗi tranh chấp thường chỉ xuất hiện vài lần trên trăm
- Assert trên **trạng thái cuối** đọc lại từ API hoặc DB, không chỉ trên response của từng request

### 13.2. Idempotency

- Gửi lại đúng một request đã thành công (cùng idempotency key nếu hệ thống có): không tạo bản ghi thứ hai, không đổi trạng thái lần nữa
- Webhook hoặc message đến hai lần: chỉ xử lý một lần
- Bấm nút nhiều lần trên UI (E2E): chỉ một request có hiệu lực

### 13.3. Bất biến nghiệp vụ (property-based và model-based)

> Thay vì viết tay từng case, mô tả **điều luôn phải đúng** rồi để công cụ sinh hàng trăm chuỗi thao tác ngẫu nhiên. Công cụ: **fast-check** (TypeScript), **Hypothesis** (Python).

- Viết bất biến dưới dạng câu kiểm được sau mỗi chuỗi thao tác. Ví dụ: tổng tiền khớp, trạng thái chỉ đi theo các cạnh hợp lệ của sơ đồ trạng thái, dữ liệu hai portal giống nhau
- Với chức năng có bảng quyết định hoặc sơ đồ trạng thái rõ ràng: dựng một **mô hình** đơn giản trong code test, sinh chuỗi thao tác, so kết quả hệ thống với kết quả mô hình
- Khi công cụ tìm ra chuỗi làm hỏng bất biến: lưu chuỗi đó thành một case cố định trong bộ hồi quy

---

## Nhóm 14: Kiểm đầu ra ngoài giao diện

### 14.1. Email và thông báo

- Môi trường test gửi email vào hộp thư bắt giữ (**Mailpit**, MailHog), không gửi ra ngoài
- Kiểm: đúng người nhận, không thiếu ai, không gửi nhầm, đúng tiêu đề, giá trị động điền đúng, không gửi trùng, gửi trong ngưỡng thời gian
- SMS, push: dùng nhà cung cấp giả hoặc chế độ sandbox, kiểm tương tự
- Thông báo trong hệ thống (chuông): kiểm qua API danh sách thông báo của từng người nhận

### 14.2. File sinh ra

- PDF: đọc nội dung bằng `pdf-parse` hoặc `pdfplumber`, so từng giá trị quan trọng (tên, số tiền, ngày giờ, danh sách dòng). Không chỉ kiểm "tải được file"
- Excel: đọc bằng `exceljs` hoặc `openpyxl`, kiểm tên cột, số dòng, giá trị, định dạng số và ngày
- DOCX: đọc bằng `mammoth` hoặc `python-docx`, kiểm biến mẫu đã được thay hết, không còn `{...}`
- File có chữ ký số: kiểm chữ ký còn hợp lệ, file không bị sửa sau khi ký

### 14.3. Nhật ký hệ thống và dữ liệu lưu

- Sau thao tác quan trọng, đọc nhật ký qua API hoặc DB: đúng người, đúng hành động, đúng giá trị cũ và mới, đúng thời điểm
- Kiểm nhật ký không sửa, không xóa được qua API

### 14.4. Dịch vụ ngoài giả lập

- Cổng thanh toán, eKYC, ký số, AI: dùng sandbox của nhà cung cấp nếu có, hoặc stub tự viết (**WireMock**, **Mockoon**, **MSW**)
- Stub phải giả lập được: thành công, lỗi, chậm quá hạn, trả dữ liệu sai định dạng, gọi lại (callback, webhook) trùng hoặc sai thứ tự
- Có ít nhất một bộ test chạy với sandbox thật của nhà cung cấp trước mỗi lần phát hành, để bắt chỗ stub lệch với thực tế

---

## Nhóm 15: Dữ liệu test, độ ổn định và chỉ số automation

### 15.1. Dựng dữ liệu theo trạng thái

- Viết **factory** tạo bản ghi ở đúng trạng thái cần test qua API hoặc seed, không đi lại toàn bộ luồng UI. Ví dụ factory "cuộc đấu đang ở vòng gia hạn thứ 2, có 3 khách đã nộp cọc"
- Dữ liệu cá nhân trong factory là dữ liệu giả, sinh theo đúng định dạng (CCCD, MST, SĐT), không dùng dữ liệu thật
- Mỗi test tự tạo và tự dọn dữ liệu của mình, có job dọn định kỳ cho dữ liệu sót lại (`Testcase_Template.md` Mục 1.10)

### 15.2. Độ ổn định của bộ test (flaky test)

- Test fail không ổn định: được chạy lại tối đa 2 lần trong CI, nhưng **mọi lần chạy lại đều được ghi nhận**
- Test fail không ổn định quá 3 lần trong 2 tuần: chuyển vào danh sách cách ly, mở ticket sửa, không xóa và không bỏ qua im lặng
- Không dùng `sleep` cố định để "chữa" flaky. Tìm điều kiện chờ đúng

### 15.3. Chỉ số theo dõi

| Chỉ số | Cách tính | Mục tiêu tham chiếu |
|---|---|---|
| Tỷ lệ TC High đã automate | Số TC High có `✅ Automated` / tổng TC High | ≥ 80% |
| Tỷ lệ TC High về tiền, kết quả, thời gian đã automate | Như trên, chỉ tính nhóm rủi ro cao | ≥ 95% |
| Phân bổ layer | Số TC theo từng layer | E2E không quá 20% số TC đã automate |
| Tỷ lệ flaky | Số lần fail không ổn định / tổng số lần chạy | < 2% |
| Thời gian chạy theo giai đoạn | Theo bảng ở Mục 0.3 | Không vượt mục tiêu |

---

## Phụ lục: Cấu trúc thư mục đề xuất

```
📁 tests/
├── 📁 smoke/                     ← Nhóm 1: Smoke & Sanity tests
│   └── smoke.spec.ts
│
├── 📁 e2e/                       ← Nhóm 2: E2E tests
│   ├── 📁 pages/                 ← Page Object Model
│   ├── 📁 fixtures/              ← Test data cố định
│   ├── 📁 helpers/               ← API helpers cho setup/cleanup
│   └── 📁 specs/                 ← Test files, tổ chức theo module
│       ├── category.spec.ts
│       └── product.spec.ts
│
├── 📁 api/                       ← Nhóm 3: API tests
│   ├── category.test.ts
│   └── product.test.ts
│
├── 📁 integration/               ← Nhóm 4: Integration tests
│
├── 📁 db/                        ← Nhóm 5: DB integrity tests
│
├── 📁 performance/               ← Nhóm 6: k6 scripts
│   ├── baseline.js
│   ├── load.js
│   └── stress.js
│
├── 📁 security/                  ← Nhóm 7: Security test scripts
│
├── 📁 contract/                  ← Nhóm 8: Pact/schema files
│
├── 📁 visual/                    ← Nhóm 10: Visual regression
│   └── snapshots/                ← Baseline images
│
├── 📁 realtime/                  ← Nhóm 12: client WebSocket
├── 📁 concurrency/               ← Nhóm 13: kịch bản đồng thời, property-based
├── 📁 outputs/                   ← Nhóm 14: kiểm email, PDF, Excel, nhật ký
├── 📁 stubs/                     ← Nhóm 14.4: stub dịch vụ ngoài
├── 📁 factories/                 ← Nhóm 15.1: dựng dữ liệu theo trạng thái
└── 📁 mobile/                    ← Nhóm 2.11: Maestro/Appium flows
```

---

## Phụ lục: Mẫu mô tả Automation Test Case theo từng loại

> Automation test case **không được mô tả bằng bảng như manual** (không có cột "Tiền điều kiện / Các bước / Kết quả mong muốn"). Thay vào đó, mỗi loại automation có cách mô tả riêng — **tên test function chính là tài liệu**. Phụ lục này giải thích cụ thể từng loại trông như thế nào trong thực tế, để khi đọc output gen ra bạn hiểu ngay phần đó đang làm gì.

---

### A. E2E / UI Automation (Playwright / Cypress)

**Cấu trúc file:**
```
tests/e2e/specs/category.spec.ts
```

**Mẫu đầy đủ:**
```typescript
import { test, expect } from '@playwright/test';
import { CategoryListPage } from '../pages/CategoryListPage';
import { CategoryFormPage } from '../pages/CategoryFormPage';
import { createCategoryAPI, deleteCategoryAPI } from '../helpers/category.api';

// ── Nhóm test tương ứng với 1 màn hình / 1 chức năng ──────────────────────
describe('Thêm mới danh mục tài sản', () => {

  // ── Mỗi it() = 1 testcase, tên mô tả rõ điều kiện và kết quả ─────────────

  /**
   * @manual   TC-DMTS-020
   * @layer    E2E
   * @priority High
   */
  test('Nhập Tên hợp lệ → lưu thành công, bản ghi xuất hiện trong danh sách', async ({ page }) => {
    // ARRANGE
    const listPage = new CategoryListPage(page);
    const formPage = new CategoryFormPage(page);
    await listPage.goto();

    // ACT
    await listPage.clickAddButton();
    await formPage.fillName('Xe máy');
    await formPage.clickSave();

    // ASSERT — UI
    await expect(formPage.toastSuccess).toContainText('Thêm mới thành công');
    await expect(listPage.rowByName('Xe máy')).toBeVisible();

    // ASSERT — Data (xác nhận DB qua API, không chỉ tin UI)
    const created = await listPage.getCreatedRecordViaAPI('Xe máy');
    expect(created.name).toBe('Xe máy');

    // CLEANUP
    await deleteCategoryAPI(created.id);
  });

  /**
   * @manual   TC-DMTS-022
   * @layer    E2E
   * @priority High
   */
  test('Để trống Tên → hiển thị lỗi bắt buộc, không lưu được', async ({ page }) => {
    const formPage = new CategoryFormPage(page);
    await formPage.goto();

    await formPage.clearName();
    await formPage.clickSave();

    await expect(formPage.errorByField('name')).toContainText('Tên danh mục không được để trống');
    await expect(formPage.toastSuccess).not.toBeVisible();
  });

  /**
   * @manual   TC-DMTS-025
   * @layer    E2E
   * @priority Medium
   */
  test('Nhập đúng 255 ký tự → lưu thành công (biên trên max-length)', async ({ page }) => {
    // ... tương tự cấu trúc trên
  });

});
```

**Cách đọc output gen:**
- Mỗi `describe()` = 1 nhóm testcase (tương ứng với cấp 1 trong Mục 1.2 của file manual)
- Mỗi `test()` / `it()` = 1 testcase cụ thể, ID manual được ghi trong `@manual`
- `@layer` cho biết đây là E2E, không phải API hay unit test
- `@priority` khớp với cột "Mức độ ưu tiên" trong file manual
- Comment block `ARRANGE / ACT / ASSERT / CLEANUP` giúp đọc hiểu luồng test mà không cần tài liệu bổ sung

---

### B. API Testing (pytest + httpx / Jest + supertest)

**Cấu trúc file:**
```
tests/api/category.test.ts      (Node.js)
tests/api/test_category.py      (Python)
```

**Mẫu Node.js (Jest + supertest):**
```typescript
describe('POST /api/v1/categories', () => {

  // TC-DMTS-020 — Happy path
  it('201: Tạo thành công với đủ field bắt buộc', async () => {
    const res = await request(app)
      .post('/api/v1/categories')
      .set('Authorization', `Bearer ${token}`)
      .send({ name: 'Xe máy', code: 'XM001' });

    expect(res.status).toBe(201);
    expect(res.body.name).toBe('Xe máy');
    expect(res.body).not.toHaveProperty('password');  // Field nhạy cảm không được lộ
    expect(res.body).toHaveProperty('id');
    expect(res.body).toHaveProperty('createdAt');
  });

  // TC-DMTS-022 — Validate: bắt buộc
  it('400: Thiếu field "name" → báo lỗi rõ field nào sai', async () => {
    const res = await request(app)
      .post('/api/v1/categories')
      .set('Authorization', `Bearer ${token}`)
      .send({ code: 'XM001' });  // Thiếu name

    expect(res.status).toBe(400);
    expect(res.body.errors).toContainEqual(
      expect.objectContaining({ field: 'name', message: expect.any(String) })
    );
  });

  // TC-DMTS-045 — Auth: không có token
  it('401: Không có token → từ chối, không trả dữ liệu', async () => {
    const res = await request(app)
      .post('/api/v1/categories')
      .send({ name: 'Xe máy', code: 'XM001' });

    expect(res.status).toBe(401);
    expect(res.body).not.toHaveProperty('id');
  });

  // TC-DMTS-030 — Validate: unique
  it('409: Trùng mã đã tồn tại → Conflict', async () => {
    // Tạo bản ghi trước
    await createCategoryAPI({ name: 'Xe đạp', code: 'XD001' });

    const res = await request(app)
      .post('/api/v1/categories')
      .set('Authorization', `Bearer ${token}`)
      .send({ name: 'Xe đạp 2', code: 'XD001' });  // Trùng code

    expect(res.status).toBe(409);
  });

});
```

**Mẫu Postman Collection (dạng cây thư mục):**
```
📁 Category API Tests
  📁 POST /api/v1/categories — Tạo mới danh mục
    ✅ [TC-DMTS-020] 201 - Tạo thành công đủ field
    ❌ [TC-DMTS-022] 400 - Thiếu field "name"
    ❌ [TC-DMTS-023] 400 - name vượt 255 ký tự
    ❌ [TC-DMTS-030] 409 - Trùng mã danh mục
    ❌ [TC-DMTS-045] 401 - Không có token
    ❌ [TC-DMTS-046] 403 - Token không đủ quyền
  📁 GET /api/v1/categories — Danh sách danh mục
    ✅ [TC-DMTS-050] 200 - Lấy danh sách thành công
    ✅ [TC-DMTS-051] 200 - Phân trang đúng (page=2, size=10)
    ❌ [TC-DMTS-052] 401 - Không có token
```

**Cách đọc output gen:**
- Mỗi `describe()` = 1 endpoint (method + path)
- Tên `it()` bắt đầu bằng **status code** → đọc ngay biết kết quả mong muốn là gì
- Prefix `[TC-DMTS-020]` trong tên test = liên kết về Manual TC ID
- ✅ = happy path, ❌ = error case (không có nghĩa là test fail — đây là test *kỳ vọng* server trả lỗi)

---

### C. Performance Testing (k6)

**Cấu trúc file:**
```
tests/performance/
  baseline.js     ← Đo thời gian phản hồi 1 user
  load.js         ← Mô phỏng nhiều user đồng thời
  stress.js       ← Tìm điểm gãy
  soak.js         ← Chạy dài để phát hiện memory leak
```

**Mẫu `load.js` — Load test:**
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

// ── Mô tả scenario: ai làm gì, bao nhiêu người, trong bao lâu ────────────
export const options = {
  scenarios: {
    // Luồng 1: Người dùng xem danh sách + tìm kiếm (chiếm 70% traffic)
    browse_and_search: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 70 },   // Tăng dần lên 70 users trong 2 phút
        { duration: '5m', target: 70 },   // Giữ 70 users trong 5 phút
        { duration: '1m', target: 0 },    // Giảm về 0
      ],
    },
    // Luồng 2: Người dùng tạo mới (chiếm 20% traffic)
    create_records: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 20 },
        { duration: '5m', target: 20 },
        { duration: '1m', target: 0 },
      ],
    },
  },

  // ── Ngưỡng pass/fail — test fail tự động nếu vượt ────────────────────
  thresholds: {
    // Toàn bộ request: p95 < 500ms
    'http_req_duration': ['p(95)<500'],
    // Riêng API danh sách: p95 < 300ms
    'http_req_duration{name:list_categories}': ['p(95)<300'],
    // Tỷ lệ lỗi < 0.1%
    'http_req_failed': ['rate<0.001'],
  },
};

// ── Nội dung từng request ──────────────────────────────────────────────────
export default function () {
  // GET danh sách — gắn tag "name" để thresholds phân biệt được
  const listRes = http.get(
    `${__ENV.BASE_URL}/api/v1/categories?page=1&size=20`,
    { tags: { name: 'list_categories' } }
  );
  check(listRes, {
    'GET /categories: status 200': (r) => r.status === 200,
    'GET /categories: có dữ liệu': (r) => JSON.parse(r.body).data.length > 0,
  });

  sleep(1); // Nghỉ 1 giây giữa các request (mô phỏng hành vi người dùng thực)
}
```

**Cách đọc output gen:**
- File performance **không có ID TC** như E2E/API — thay vào đó, tên `scenario` mô tả *ai đang làm gì*
- `thresholds` = tiêu chí pass/fail (thay cho cột "Kết quả mong muốn" của manual)
- `check()` = assertion trong từng request (test có pass không)
- Output sau khi chạy k6 cho thấy: p50/p95/p99 thực tế, error rate, số request/s — đối chiếu với bảng SLA tại Nhóm 0.4

---

### D. Security Testing (OWASP ZAP — chế độ CI)

**Cấu trúc file:**
```
tests/security/
  zap-baseline.yaml     ← Cấu hình scan
  zap-full-scan.yaml    ← Scan đầy đủ
```

**Mẫu GitHub Actions chạy ZAP:**
```yaml
# .github/workflows/security-scan.yml
- name: OWASP ZAP Baseline Scan
  uses: zaproxy/action-baseline@v0.10.0
  with:
    target: 'https://staging.yourapp.com'
    rules_file_name: 'tests/security/zap-rules.tsv'
    cmd_options: '-a'   # Bao gồm cả AJAX spider

# zap-rules.tsv — Cấu hình rule nào fail, warn, hay ignore
# Rule ID  Action  Description
# 10016    FAIL    Web Browser XSS Protection Not Enabled
# 10017    FAIL    Cross-Domain JavaScript Source File Inclusion
# 10020    FAIL    X-Frame-Options Header Not Set
# 10038    WARN    Content Security Policy (CSP) Header Not Set
# 40012    FAIL    Cross Site Scripting (Reflected)
# 40014    FAIL    Cross Site Scripting (Persistent)
# 40018    FAIL    SQL Injection
```

**Cách đọc output gen:**
- Security test không có file spec.ts như E2E — tool tự scan và sinh report
- Mỗi **Alert** trong report ZAP = 1 lỗ hổng phát hiện được, có Risk level (High/Medium/Low/Info)
- Rule ID liên kết về OWASP catalog để tra thêm thông tin
- Kết quả: **0 High alert = pass**, có bất kỳ High alert nào = **fail build**

---

### E. Visual Regression Testing (Playwright Screenshot)

**Cấu trúc file:**
```
tests/visual/
  category-list.visual.ts
  snapshots/                ← Ảnh baseline (commit vào repo)
    category-list-desktop.png
    category-list-mobile.png
```

**Mẫu:**
```typescript
import { test, expect } from '@playwright/test';

test.describe('Visual regression — Danh sách danh mục', () => {

  test('Desktop 1440px — layout không thay đổi so với baseline', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto('/categories');

    // Đợi data load xong, animation kết thúc
    await page.waitForSelector('[data-testid="category-table"]');
    await page.waitForTimeout(300); // Đợi animation

    // Mask vùng dynamic content trước khi chụp
    await page.evaluate(() => {
      document.querySelectorAll('[data-visual-test="ignore"]')
        .forEach(el => (el as HTMLElement).style.visibility = 'hidden');
    });

    // Chụp và so sánh với baseline — fail nếu khác > 0.1%
    await expect(page).toHaveScreenshot('category-list-desktop.png', {
      maxDiffPixelRatio: 0.001,
    });
  });

  test('Mobile 375px — layout responsive không vỡ', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 812 });
    await page.goto('/categories');
    await page.waitForSelector('[data-testid="category-table"]');

    await expect(page).toHaveScreenshot('category-list-mobile.png', {
      maxDiffPixelRatio: 0.001,
    });
  });

});
```

**Cách đọc output gen:**
- Không có ID TC — visual test được nhận dạng bằng **tên màn hình + viewport**
- Khi test fail: Playwright sinh ra file diff ảnh (baseline vs actual vs diff) để xem trực quan vùng nào thay đổi
- Nếu thay đổi **có chủ đích** (redesign): chạy `npx playwright test --update-snapshots` để cập nhật baseline
- Nếu thay đổi **ngoài ý muốn**: fix CSS rồi chạy lại cho đến khi pass

---

### F. Tổng hợp: Output gen có dạng gì theo từng loại

Khi tôi gen test case automation cho một chức năng cụ thể, output sẽ gồm:

| Loại | Output gen ra | Bạn đọc và hiểu là |
|---|---|---|
| **E2E** | Danh sách `describe/test()` block với tên mô tả rõ + `@manual TC-ID` | Danh sách test script cần viết, mỗi dòng = 1 test function |
| **API** | Danh sách `describe/it()` theo endpoint, prefix status code + TC-ID | Danh sách request/assertion cần viết, tổ chức theo endpoint |
| **Performance** | Danh sách scenario cần viết (baseline/load/stress/soak) + threshold tham chiếu từ Nhóm 0.4 | Danh sách k6 script cần viết, ngưỡng pass/fail cần set |
| **Security** | Danh sách rule cần bật trong ZAP config + endpoint cần scan | Cấu hình scan cần setup trong CI/CD |
| **Visual** | Danh sách màn hình × viewport cần chụp baseline + vùng dynamic cần mask | Danh sách visual test cần viết, biết trước phải xử lý dynamic content ở đâu |
| **Smoke** | Danh sách health check + CRUD smoke theo đúng endpoint thực tế của module | Bộ test chạy sau mỗi deploy, cần viết trước ngày go-live |

---

*File này là tài liệu sống — cập nhật khi có thay đổi về tool, strategy, hoặc ngưỡng SLA của dự án.*
*Phiên bản hiện tại bao phủ: 15 nhóm automation, từ Smoke test đến quản lý độ ổn định của bộ test.*
*Xem `Testcase_Template.md` cho checklist test manual tương ứng, và `QA-Auction-Automation-Checklist.md` cho phần riêng của dự án đấu giá.*

