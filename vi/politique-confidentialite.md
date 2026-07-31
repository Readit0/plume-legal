# Chính sách quyền riêng tư của Plume

**Cập nhật lần cuối: ngày 31 tháng 7 năm 2026** — Phiên bản 1.0

---

## Ai chịu trách nhiệm về dữ liệu của bạn

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Liên hệ: sogacmoi7@gmail.com

Ứng dụng được phát hành trên Google Play dưới tên nhà phát hành **openfunword**.

Chính sách này mô tả những gì ứng dụng Plume thực sự làm trong phiên bản hiện tại. Nó được viết ra từ việc đọc mã nguồn của ứng dụng, chứ không phải từ một mẫu văn bản chung chung.

---

## Trong một phút

Plume giúp bạn viết: ứng dụng viết lại văn bản của bạn ngay trong ứng dụng mà bạn đang gõ, và có thể dịch văn bản hiển thị trên màn hình.

Ba điều cần nhớ:

1. **Plume không lưu giữ bất kỳ văn bản nào của bạn trên máy chủ của mình.** Không lưu văn bản đã được viết lại, cũng không lưu văn bản đọc được trên màn hình. Chúng tôi không giữ bản sao, cũng không giữ nhật ký.
2. **Tùy theo bộ máy xử lý bạn chọn, văn bản của bạn rời khỏi hoặc không rời khỏi điện thoại.** Hai bộ máy (Bộ công cụ cục bộ và AI cục bộ) hoạt động hoàn toàn trên thiết bị. Bộ máy thứ ba (AI đám mây) gửi văn bản đến một dịch vụ trí tuệ nhân tạo **đặt bên ngoài Liên minh châu Âu**. Bạn là người lựa chọn, và AI đám mây không bao giờ được kích hoạt nếu không có sự đồng ý rõ ràng của bạn.
3. **Plume cần những quyền rất mạnh** (đọc nội dung hiển thị trong các ứng dụng khác, chụp màn hình). Dưới đây chúng tôi giải thích chính xác các quyền đó dùng để làm gì và không dùng để làm gì.

---

## 1. Plume đọc gì trên màn hình của bạn, và đọc khi nào

### 1.1 Dịch vụ trợ năng

Để viết lại văn bản của bạn ngay tại nơi bạn đang viết, Plume sử dụng dịch vụ trợ năng của Android. Đây là quyền do chính bạn bật lên trong phần cài đặt của điện thoại, sau một màn hình giải thích mà Plume hiển thị cho bạn **trước khi** yêu cầu quyền đó.

Cụ thể:

- **Khi không hoạt động**, Plume chỉ biết ứng dụng nào đang mở và biết thời điểm bạn đặt con trỏ vào một ô nhập liệu. Đó là điều làm cho capsule nổi xuất hiện — và chỉ xuất hiện trong những ứng dụng do chính bạn thiết lập.
- **Nội dung của ô nhập liệu chỉ được đọc đúng vào khoảnh khắc bạn chạm vào capsule**, để được viết lại rồi thay thế ngay tại chỗ.
- **Các ô mật khẩu bị loại trừ.** Ứng dụng nhận diện các ô thuộc loại mật khẩu (kể cả mã số và các ô trên web) và từ chối đọc chúng.
- Quyền này **không cho phép chụp bất kỳ hình ảnh nào** của màn hình bạn.
- Plume **không bao giờ bấm thay bạn** trong một ứng dụng khác: nó thay thế văn bản của một ô nhập liệu, không làm gì hơn.

Hai tính năng do chính bạn bật lên — **Đọc Có Hỗ Trợ ở chế độ Văn bản** và **dịch tin nhắn nhận được** — đọc liên tục văn bản hiển thị trong suốt thời gian chúng chạy, và dừng lại ngay khi bạn tắt chúng.

Nếu bạn từ chối dịch vụ trợ năng, Plume vẫn dùng được: bạn có thể chọn một đoạn văn bản rồi dùng mục "Plume" trong trình đơn chọn văn bản của Android, hoặc chia sẻ một đoạn văn bản sang Plume.

### 1.2 Chụp màn hình (Đọc Có Hỗ Trợ)

Đọc Có Hỗ Trợ phủ một bản dịch lên trên văn bản hiển thị — chẳng hạn các bong bóng thoại của một truyện tranh. Tính năng này cần nhìn thấy hình ảnh của màn hình.

- Tính năng này **mặc định bị tắt** và chỉ hoạt động trong những ứng dụng mà bạn đã cho phép một cách rõ ràng, từng ứng dụng một.
- **Android yêu cầu sự đồng ý của riêng nó ở mỗi lần bắt đầu phiên.** Đây không phải một quyền được cấp một lần cho mãi mãi: mỗi phiên đều đòi hỏi một sự chấp thuận mới. Plume không bao giờ tìm cách dùng lại hay lách sự chấp thuận đó.
- Trong suốt phiên, **một thông báo thường trực và một chỉ báo của hệ thống luôn hiển thị**. Plume không thể chụp màn hình của bạn một cách kín đáo.
- Phiên **tự động dừng khi màn hình bị khóa**, và dừng ngay lập tức khi chính bạn dừng nó.
- Những ứng dụng bảo vệ phần hiển thị của mình (ứng dụng ngân hàng, trình quản lý mật khẩu) được **chính Android che đi** trước khi Plume nhận được bất cứ thứ gì. Đây là một biện pháp bảo vệ của hệ thống, có thật nhưng không đầy đủ: không phải mọi ứng dụng nhạy cảm đều bật nó. Vì vậy chúng tôi không trình bày biện pháp này như một bảo đảm tuyệt đối.
- **Các hình ảnh chụp được không bao giờ được lưu lại hay gửi đi.** Mỗi hình ảnh được phân tích trong bộ nhớ để trích xuất văn bản, rồi bị loại bỏ. Không có hình ảnh nào rời khỏi điện thoại của bạn, không bao giờ, dù bạn chọn bộ máy xử lý nào.

---

## 2. Những gì ở lại trên điện thoại của bạn và những gì đi ra ngoài

Đây là sự phân biệt quan trọng nhất trong chính sách này, và chính bạn là người kiểm soát nó.

### 2.1 Những bộ máy không gửi gì ra ngoài

- **Bộ công cụ cục bộ** (nhận dạng và dịch văn bản ngoại tuyến) hoạt động hoàn toàn trên thiết bị.
- **AI cục bộ** là một mô hình trí tuệ nhân tạo được tải xuống một lần rồi lưu trên điện thoại của bạn (khoảng 720 MB). Mô hình này chạy trên thiết bị của bạn.

Với hai bộ máy này, **văn bản được đọc hoặc được viết lại không rời khỏi điện thoại của bạn.** Không có bất kỳ lệnh gọi mạng nào liên quan đến nội dung văn bản của bạn.

### 2.2 Bộ máy AI đám mây

Khi bạn chọn AI đám mây, hoặc khi thiết bị của bạn không đủ mạnh cho AI cục bộ, văn bản liên quan được truyền đến máy chủ của chúng tôi, rồi đến một dịch vụ trí tuệ nhân tạo của bên thứ ba.

**Cần nói rõ về hành trình thực sự của nó:**

- Văn bản đi qua hạ tầng của chúng tôi (Supabase), đặt tại **Liên minh châu Âu** (khu vực Trung Âu, Frankfurt).
- Sau đó nó được truyền đến **openrouter.ai**, một bên trung gian định tuyến **đặt bên ngoài Liên minh châu Âu**, nơi giao cho mô hình **Mistral Small** xử lý.
- **Vì vậy đây là một hoạt động chuyển dữ liệu ra ngoài Liên minh châu Âu.** Chúng tôi không nói khác đi, và chúng tôi không đưa ra bất kỳ lời hứa nào về việc lưu trữ tại châu Âu cho bước này.
- **Plume không lưu giữ văn bản của bạn.** Không một hàm máy chủ nào của chúng tôi ghi lại nội dung văn bản của bạn: chúng tôi chỉ ghi lại một mã kỹ thuật của yêu cầu và mã định danh thiết bị của bạn, để đếm hạn mức của bạn và phát hiện hành vi lạm dụng.
- **Những gì các nhà cung cấp này làm ở phía họ, chúng tôi không thể bảo đảm.** Chúng tôi thà nói thẳng với bạn còn hơn hứa hẹn một mức lưu giữ bằng không mà chúng tôi không ở vị thế kiểm chứng được.

**AI đám mây không bao giờ tự kích hoạt.** Một màn hình đồng ý riêng giải thích cho bạn những điểm này trước lần gửi đầu tiên, và không có gì được gửi đi chừng nào bạn chưa chấp nhận. Nếu AI cục bộ thất bại, Plume không âm thầm chuyển sang đám mây: ứng dụng báo cho bạn biết và chờ quyết định của bạn. Bạn có thể rút lại sự đồng ý này bất cứ lúc nào trong phần cài đặt.

Văn bản được gửi đi có giới hạn trần: 1.200 ký tự cho một lượt viết lại, 4.000 ký tự cho một lượt phân tích màn hình.

---

## 3. Những dữ liệu chúng tôi lưu giữ

Chúng tôi **không sử dụng bất kỳ công cụ phân tích người dùng nào, bất kỳ trình theo dõi quảng cáo của bên thứ ba nào, bất kỳ công cụ báo cáo sự cố nào**. Ứng dụng không chứa SDK đo lường.

Sau đây là toàn bộ những gì được lưu trên máy chủ của chúng tôi:

| Dữ liệu | Vì sao | Thời hạn |
|---|---|---|
| **Mã định danh thiết bị** (một dãy số ngẫu nhiên do Plume tạo ra, không liên hệ với danh tính của bạn hay với một mã quảng cáo nào) | Gắn một thiết bị với một tài khoản, áp dụng hạn mức, chặn hành vi lạm dụng | Cho đến khi bạn xóa tài khoản |
| **Địa chỉ email của tài khoản** (nếu bạn tạo tài khoản bằng email hoặc qua Google) | Xác thực bạn, gắn gói đăng ký của bạn | Cho đến khi bạn xóa tài khoản |
| **Bộ đếm mức sử dụng** (số lượt viết lại mỗi ngày và mỗi tháng — là những con số, không phải văn bản) | Áp dụng hạn mức | Cho đến khi bạn xóa tài khoản |
| **Lịch sử mua hàng** (mã giao dịch Google Play, ngày tháng, trạng thái gói đăng ký) | Cho bạn quyền truy cập vào những gì bạn đã trả tiền, quản lý việc gia hạn, tuân thủ nghĩa vụ kế toán của chúng tôi | Được giữ lại kể cả sau khi xóa tài khoản, nhưng **tách rời khỏi danh tính của bạn** (xem §6) |
| **Góp ý gửi tự nguyện** (nếu bạn gửi cho chúng tôi một đề xuất persona từ trong ứng dụng) | Cải thiện danh mục. Những góp ý này không bao giờ được công bố. | Cho đến khi bạn xóa tài khoản |
| **Tín hiệu kỹ thuật về lạm dụng** (vượt hạn mức nhiều lần, kiểm tra tính toàn vẹn thất bại — không kèm bất kỳ văn bản nào) | An ninh, chống gian lận | Được tách rời khỏi danh tính của bạn khi xóa tài khoản |
| **Ngôn ngữ và phiên bản ứng dụng** | Cung cấp đúng nội dung | Cho đến khi bạn xóa tài khoản |

**Những gì chúng tôi không thu thập:** tên của bạn, danh bạ của bạn, vị trí của bạn, sổ địa chỉ của bạn, ảnh của bạn, lịch của bạn, lịch sử các ứng dụng của bạn. Plume không yêu cầu bất kỳ quyền nào trong số đó.

**Những gì chỉ ở lại trên điện thoại của bạn:** các persona bạn tự tạo cùng ảnh đại diện của chúng, các thiết lập của bạn, các quy tắc theo từng ứng dụng của bạn, bộ nhớ đệm bản dịch của Đọc Có Hỗ Trợ (được xóa vào cuối mỗi phiên). Không thứ nào trong số đó được gửi đến máy chủ của chúng tôi.

---

## 4. Nhập liệu bằng giọng nói

Một nút micrô cho phép bạn đọc thay vì gõ. Quyền truy cập micrô được yêu cầu **đúng vào lúc bạn bấm nút đó**, không bao giờ khi khởi động, và micrô chỉ mở ra vào đúng khoảnh khắc ấy. Plume không bao giờ nghe ở chế độ nền.

**Plume không nhận, không lưu trữ và không truyền đi bất kỳ bản ghi âm nào.** Việc nhận dạng giọng nói được giao cho bộ máy nhận dạng giọng nói tích hợp sẵn trong điện thoại của bạn (bộ máy của Android). Plume chỉ nhận lại phần văn bản đã được chuyển thành chữ.

**Một điểm quan trọng và thành thật:** bộ máy hệ thống này thuộc về điện thoại của bạn, thường là của Google. Tùy theo thiết bị, các thiết lập và các gói ngôn ngữ đã cài đặt, **nó có thể truyền âm thanh đến máy chủ của nhà phát hành hệ thống** để chuyển thành văn bản. Việc xử lý này nằm ngoài tầm với của Plume và thuộc phạm vi chính sách quyền riêng tư của nhà phát hành hệ điều hành trên máy bạn. Do đó chúng tôi không thể khẳng định rằng giọng nói của bạn ở lại trên thiết bị — điều đó phụ thuộc vào điện thoại của bạn, không phụ thuộc vào chúng tôi.

Nếu bạn từ chối quyền micrô, việc nhập liệu bằng bàn phím dĩ nhiên vẫn dùng được.

---

## 5. Quảng cáo

Dịch vụ miễn phí trong một giới hạn sử dụng nhất định mỗi ngày. Vượt quá giới hạn đó, bạn **có thể chọn** xem một quảng cáo có thưởng để mở khóa thêm lượt sử dụng. Điều này không bao giờ bị áp đặt: nếu bạn không xem quảng cáo, bạn đơn giản vẫn giữ những gì bạn có quyền được hưởng.

- Quảng cáo do **Google AdMob** cung cấp.
- Chúng chỉ xuất hiện **trong chính ứng dụng Plume**, không bao giờ trong capsule nổi và không bao giờ đè lên một ứng dụng khác.
- **Người đăng ký gói không thấy bất kỳ quảng cáo nào.**
- Tại Khu vực Kinh tế châu Âu, Vương quốc Anh và Thụy Sĩ, một biểu mẫu đồng ý do một nền tảng được Google chứng nhận cung cấp sẽ được hiển thị cho bạn **trước quảng cáo đầu tiên**. Chừng nào lựa chọn của bạn chưa được thu thập, không một quảng cáo nào được yêu cầu. Nếu bạn từ chối, quảng cáo vẫn ở dạng **không được cá nhân hóa** và **không tính năng nào bị lấy đi khỏi bạn**. Bạn có thể thay đổi lựa chọn này bất cứ lúc nào trong phần cài đặt.
- Để ghi có phần thưởng cho bạn một cách đáng tin cậy, mã định danh thiết bị Plume của bạn được truyền cho AdMob. Ngoài ra Google có thể thu thập dữ liệu của riêng họ theo chính sách quyền riêng tư của họ.

*Vào thời điểm soạn thảo văn bản này, việc hiển thị quảng cáo đang bị tắt ở phía máy chủ. Mục này mô tả cách hoạt động ngay khi nó được bật lên.*

---

## 6. Gói đăng ký và mua hàng

Các gói đăng ký và các gói nội dung được bán **qua Google Play**. Chúng tôi không bao giờ thấy thông tin ngân hàng của bạn: chúng do Google xử lý, và Google là bên bán theo nghĩa lập hóa đơn.

Chúng tôi nhận từ Google một chứng từ mua hàng mà máy chủ của chúng tôi kiểm tra, và chúng tôi lưu dấu vết của nó (mã giao dịch, ngày tháng, trạng thái). Dấu vết này được lưu vì lý do kế toán và để ngăn một lần mua được dùng hai lần — nhưng nó được **tách rời khỏi danh tính của bạn** khi bạn xóa tài khoản.

---

## 7. Các quyền của bạn

Bạn có quyền truy cập, quyền chỉnh sửa, quyền xóa, quyền hạn chế xử lý, quyền phản đối và quyền chuyển dữ liệu theo quy định của GDPR.

**Cách đơn giản nhất và nhanh nhất: việc xóa được tích hợp ngay trong ứng dụng.**
Cài đặt → Quyền riêng tư → Xóa dữ liệu của tôi. Việc xóa được **thực hiện ngay lập tức**, không bị đưa vào hàng chờ. Chi tiết về những gì bị xóa và những gì được giữ lại nằm trong trang chuyên biệt của chúng tôi: `https://readit0.github.io/plume-legal/suppression-compte`.

Bạn cũng có thể xóa tài khoản **mà không cần cài đặt ứng dụng**, bằng cách gửi thư đến sogacmoi7@gmail.com.

Với mọi yêu cầu khác, xin gửi thư đến **sogacmoi7@gmail.com**. Chúng tôi trả lời trong vòng một tháng.

**Cơ sở pháp lý:** việc thực hiện hợp đồng (cung cấp dịch vụ mà bạn yêu cầu, quản lý gói đăng ký của bạn), sự đồng ý của bạn (dịch vụ trợ năng, chụp màn hình, gửi dữ liệu đến AI đám mây, quảng cáo được cá nhân hóa), lợi ích hợp pháp của chúng tôi (an ninh, chống gian lận) và các nghĩa vụ pháp lý của chúng tôi (kế toán).

Bạn có thể khiếu nại đến **CNIL** (www.cnil.fr), cơ quan giám sát của nhà phát hành, hoặc, **nếu bạn cư trú trong Liên minh châu Âu**, đến cơ quan giám sát của nước bạn cư trú — Điều 77 của GDPR cho bạn quyền lựa chọn.

---

## 8. Người chưa thành niên

Plume là một công cụ hỗ trợ viết, dành cho người dùng **từ 16 tuổi trở lên**. Chúng tôi không cố ý thu thập dữ liệu của trẻ em dưới 16 tuổi và ứng dụng không được thiết kế cũng không được quảng bá cho các em. Nếu bạn là người có quyền làm cha mẹ và cho rằng con bạn đã gửi dữ liệu cho chúng tôi, xin gửi thư đến sogacmoi7@gmail.com: chúng tôi sẽ xóa tài khoản đó.

Vì ứng dụng cho phép viết lại văn bản tự do và có hiển thị quảng cáo, ứng dụng không đủ điều kiện tham gia các chương trình dành cho gia đình của Google Play.

---

## 9. Bên xử lý dữ liệu và bên nhận dữ liệu

| Nhà cung cấp | Vai trò | Ở đâu |
|---|---|---|
| **Supabase** | Lưu trữ cơ sở dữ liệu, xác thực, các hàm máy chủ | Liên minh châu Âu (Frankfurt) |
| **OpenRouter** | Định tuyến các yêu cầu đến mô hình AI | **Ngoài Liên minh châu Âu** |
| **Mistral AI** (qua OpenRouter) | Mô hình xử lý văn bản (Mistral Small) | Xử lý qua bên trung gian nêu trên |
| **Google Play / Google Billing** | Thanh toán, gói đăng ký | Google Ireland / Hoa Kỳ |
| **Google AdMob** | Quảng cáo có thưởng | Google Ireland / Hoa Kỳ |
| **Google (các dịch vụ hệ thống của điện thoại)** | Nhận dạng giọng nói, các gói dịch ngoại tuyến | Tùy theo thiết bị của bạn |

**Chúng tôi không bán bất kỳ dữ liệu nào và không nhượng bất kỳ dữ liệu nào cho các bên môi giới dữ liệu.**

**Chuyển dữ liệu ra ngoài Liên minh châu Âu:** việc sử dụng OpenRouter, Google Play và AdMob kéo theo một hoạt động chuyển dữ liệu ra ngoài Liên minh châu Âu. Khung pháp lý của các hoạt động chuyển này (điều khoản hợp đồng tiêu chuẩn, quyết định về mức độ bảo vệ tương xứng) **phải được một chuyên gia kiểm tra và ghi thành văn bản trước khi công bố** — xem ghi chú ở cuối tài liệu.

---

## 10. An ninh

Các trao đổi giữa ứng dụng và máy chủ của chúng tôi được mã hóa (HTTPS/TLS). Việc truy cập dữ liệu trong cơ sở dữ liệu bị giới hạn bởi các quy tắc phía máy chủ: các hàm nhạy cảm không thể được gọi từ ứng dụng. Không hệ thống nào an toàn tuyệt đối, nhưng không một văn bản nào bạn viết lại được lưu ở chỗ chúng tôi — điều đó tự nó giới hạn những gì một vụ xâm nhập có thể tiết lộ.

---

## 11. Sửa đổi

Mọi sửa đổi của chính sách này sẽ được công bố tại địa chỉ `https://readit0.github.io/plume-legal` kèm một ngày mới. Trong trường hợp có thay đổi quan trọng về đường đi của dữ liệu của bạn, chúng tôi sẽ thông báo cho bạn trong ứng dụng.

---

## Điều kiện chung

Các điều kiện sử dụng dịch vụ (hạn mức, gói đăng ký, hủy đăng ký) nằm trong một tài liệu riêng: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Cần được một chuyên gia rà soát
>
> Tài liệu này được soạn ra bằng cách đo lường hành vi thực tế của ứng dụng, nhưng **nó không do một luật sư soạn thảo**. Bốn điểm cần ý kiến chuyên môn trước tiên:
>
> 1. **Việc chuyển dữ liệu ra ngoài Liên minh châu Âu** đến OpenRouter. Đây là điểm nhạy cảm nhất: cần xác định cơ chế chuyển dữ liệu được áp dụng, kiểm tra rằng có một thỏa thuận xử lý dữ liệu với nhà cung cấp này, và ghi điều đó vào đây. Chừng nào việc đó chưa được làm, tài liệu này mô tả hoạt động chuyển dữ liệu mà không khẳng định rằng nó đã có khung pháp lý bảo đảm.
> 2. **Các cơ sở pháp lý** được chọn ở §7, đặc biệt là sự phân chia giữa sự đồng ý và lợi ích hợp pháp đối với dịch vụ trợ năng.
> 3. **Độ tuổi tối thiểu** (16 tuổi) và tính nhất quán của nó với bảng câu hỏi phân loại nội dung của Google Play.
> 4. **Nội dung nêu về AI** theo quy định của châu Âu về trí tuệ nhân tạo (nghĩa vụ minh bạch đối với một hệ thống có rủi ro hạn chế).

---

Tài liệu này là bản dịch của phiên bản tiếng Pháp, có tại địa chỉ https://readit0.github.io/plume-legal/. Bản dịch được cung cấp để bạn tham khảo. Nếu có điểm khác biệt, xin liên hệ với chúng tôi qua sogacmoi7@gmail.com.
