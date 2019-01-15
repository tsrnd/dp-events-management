
-- Table Definition ----------------------------------------------
CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL UNIQUE,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS auth_user_pkey ON auth_user( id );
CREATE UNIQUE INDEX IF NOT EXISTS auth_user_username_key ON auth_user(username);

-- Table Definition ----------------------------------------------
CREATE TABLE IF NOT EXISTS tbl_group (
    id SERIAL PRIMARY KEY,
    group_name character varying(100) NOT NULL,
    root_id integer,
    is_delete boolean NOT NULL
);
COMMENT ON COLUMN tbl_group.group_name IS 'Tên nhóm không được phép trùng nhau trên cùng 1 level(Group riêng hoặc là group trong cùng tổ chức)';
COMMENT ON COLUMN tbl_group.root_id IS 'Trong trường hợp nhóm này thuộc 1 tổ chức(Group) thì phải thiết lập giá trị cha của nó.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS tbl_group_pkey ON tbl_group(id int4_ops);

-- Table Definition ----------------------------------------------
CREATE TABLE IF NOT EXISTS tbl_group_user (
    id SERIAL PRIMARY KEY,
    user_id integer NOT NULL REFERENCES auth_user(id),
    group_id integer NOT NULL REFERENCES tbl_group(id),
    is_delete boolean NOT NULL DEFAULT false
);
COMMENT ON COLUMN tbl_group_user.user_id IS 'Account login.';
COMMENT ON COLUMN tbl_group_user.group_id IS 'Liên kết với Group.';
COMMENT ON COLUMN tbl_group_user.is_delete IS 'Thiết lập cờ cho trường hợp xoá mềm.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS tbl_group_user_pkey ON tbl_group_user(id int4_ops);

-- Table Definition ----------------------------------------------

CREATE TABLE IF NOT EXISTS tbl_invite_member (
    id SERIAL PRIMARY KEY,
    owner integer NOT NULL REFERENCES auth_user(id),
    user_id integer NOT NULL REFERENCES auth_user(id),
    invite_link text,
    time_create timestamp with time zone,
    expire_time timestamp with time zone,
    is_confirm boolean NOT NULL DEFAULT false,
    invite_type smallint NOT NULL,
    is_delete boolean NOT NULL DEFAULT false
);
COMMENT ON COLUMN tbl_invite_member.invite_type IS '- 1: Invite join event. - 2: Invite join group. - 0: Other.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS tbl_invite_member_pkey ON tbl_invite_member(id int4_ops);

-- Table Definition ----------------------------------------------

CREATE TABLE tbl_events (
    id SERIAL PRIMARY KEY,
    title character varying(200) NOT NULL,
    start_date date NOT NULL,
    start_time time with time zone,
    end_date date NOT NULL,
    end_time time with time zone,
    is_daily boolean NOT NULL DEFAULT false,
    is_all_day boolean NOT NULL DEFAULT false,
    location text,
    is_notification boolean DEFAULT false,
    time_notification character varying(20),
    owner integer NOT NULL REFERENCES auth_user(id),
    event_content text,
    file_attack text,
    guest_can_invite boolean NOT NULL DEFAULT true,
    view_all_guest boolean NOT NULL DEFAULT true,
    item_preparing text,
    is_public boolean,
    is_cancel boolean NOT NULL DEFAULT false,
    is_delete boolean NOT NULL DEFAULT false,
    time_create timestamp with time zone NOT NULL,
    last_edit timestamp with time zone NOT NULL,
    user_edit integer NOT NULL REFERENCES auth_user(id),
    status smallint
);
COMMENT ON COLUMN tbl_events.title IS 'Tiêu đề giới thiệu cho sự kiện sắp diễn ra.';
COMMENT ON COLUMN tbl_events.start_date IS 'Ngày bắt đầu.';
COMMENT ON COLUMN tbl_events.start_time IS 'Giờ bắt đầu.';
COMMENT ON COLUMN tbl_events.end_date IS 'Ngày kết thúc.';
COMMENT ON COLUMN tbl_events.end_time IS 'Giờ kết thúc.';
COMMENT ON COLUMN tbl_events.is_daily IS 'Có phải là diễn ra hàng ngày hay không?';
COMMENT ON COLUMN tbl_events.is_all_day IS 'Sự kiện có diễn ra cả ngày hay không? Trường hợp là True thì phải thiết lập start_time và end_time là null.';
COMMENT ON COLUMN tbl_events.location IS 'Địa điểm diễn ra sự kiện (sẽ xác định bằng Google Map API)';
COMMENT ON COLUMN tbl_events.is_notification IS 'Có thông báo trước khi diễn ra sự kiện hay không?';
COMMENT ON COLUMN tbl_events.time_notification IS 'Thời gian thông báo trước khi diễn ra sự kiện. -m  -h -d.';
COMMENT ON COLUMN tbl_events.owner IS 'Người tạo ra sự kiện.';
COMMENT ON COLUMN tbl_events.event_content IS 'Giới thiệu về sự kiện / lịch sử / ý nghĩa của sự kiện.';
COMMENT ON COLUMN tbl_events.file_attack IS 'Danh sách địa chỉ đầy đủ của các file đính kèm. Có thể là list được bố trí theo dạng XML(khá khó xử lý)';
COMMENT ON COLUMN tbl_events.guest_can_invite IS 'Cho phép những người trong ban tổ chức được phép mời người khác.';
COMMENT ON COLUMN tbl_events.view_all_guest IS 'Cho phép những người trong ban tổ chức có thể xem tất cả những người còn lại. (Không có chức năng xem tất cả các member joined)';
COMMENT ON COLUMN tbl_events.item_preparing IS 'Những trang bị cần chuẩn bị trước. Bố trí theo dạng Checkbox để kiểm tra.';
COMMENT ON COLUMN tbl_events.is_public IS 'Xác nhận loại sự kiện này là dành cho mọi người hay là cá nhân.';
COMMENT ON COLUMN tbl_events.is_cancel IS 'Sự kiện bị huỷ vì lý do nào đó.';
COMMENT ON COLUMN tbl_events.is_delete IS 'Thiết lập cờ cho trường hợp xoá mềm.';
COMMENT ON COLUMN tbl_events.last_edit IS 'Thời điểm chỉnh sửa gần nhất.';
COMMENT ON COLUMN tbl_events.user_edit IS 'Người chỉnh sửa cuối cùng.';
COMMENT ON COLUMN tbl_events.status IS 'Trạng thái của sự kiện. 0: Bản draft - 1: Waiting - 2: Cancel - 3: Done. Những trạng thái khác sẽ đề cập đến sau.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS tbl_events_pkey ON tbl_events(id int4_ops);

-- Table Definition ----------------------------------------------
CREATE TABLE tbl_events_history (
    id SERIAL PRIMARY KEY,
    title character varying(200) NOT NULL,
    start_date date NOT NULL,
    start_time time with time zone,
    end_date date NOT NULL,
    end_time time with time zone,
    is_daily boolean NOT NULL DEFAULT false,
    is_all_day boolean NOT NULL DEFAULT false,
    location text,
    is_notification boolean DEFAULT false,
    time_notification character varying(20),
    owner integer NOT NULL REFERENCES auth_user(id),
    event_content text,
    file_attack text,
    guest_can_invite boolean NOT NULL DEFAULT true,
    view_all_guest boolean NOT NULL DEFAULT true,
    item_preparing text,
    is_public boolean,
    is_cancel boolean NOT NULL DEFAULT false,
    is_delete boolean NOT NULL DEFAULT false,
    time_create timestamp with time zone NOT NULL,
    last_edit timestamp with time zone NOT NULL,
    user_edit integer NOT NULL REFERENCES auth_user(id),
    event_id integer NOT NULL REFERENCES tbl_events(id)
);
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS tbl_events_history_pkey ON tbl_events_history(id int4_ops);


-- Table Definition ----------------------------------------------
CREATE TABLE tbl_event_members (
    id SERIAL PRIMARY KEY,
    event_id integer NOT NULL REFERENCES tbl_events(id),
    user_id integer NOT NULL REFERENCES auth_user(id),
    is_going boolean NOT NULL DEFAULT false,
    is_delete boolean DEFAULT false,
    invite_id integer
);
COMMENT ON COLUMN tbl_event_members.event_id IS 'Sự kiện cho phép add thêm người tham gia.';
COMMENT ON COLUMN tbl_event_members.user_id IS 'Liên kết với table user để lấy thông tin cụ thể.';
COMMENT ON COLUMN tbl_event_members.is_going IS 'Xác nhận trạng thái tham gia của các thành viên. Mặc định khi chưa confirm sẽ là FALSE.';
COMMENT ON COLUMN tbl_event_members.is_delete IS 'Cờ trạng thái cho trường hợp xoá mềm.';
COMMENT ON COLUMN tbl_event_members.invite_id IS 'Ghi nhận tham gia sự kiện thông qua lời mời.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS tbl_event_guests_pkey ON tbl_event_members(id int4_ops);

-- Table Definition ----------------------------------------------
CREATE TABLE tbl_notifications (
    id SERIAL PRIMARY KEY,
    notify_link text,
    notify_status boolean DEFAULT false,
    user_id integer REFERENCES auth_user(id),
    is_delete boolean DEFAULT false
);
COMMENT ON COLUMN tbl_notifications.notify_link IS 'URL chỉ tới sự kiện / group / invite được gửi tới member.';
COMMENT ON COLUMN tbl_notifications.notify_status IS 'Trạng thái của thông báo. Đã đọc hay chưa?';
COMMENT ON COLUMN tbl_notifications.user_id IS 'Member nhận được thông báo.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX IF NOT EXISTS tbl_notifications_pkey ON tbl_notifications(id int4_ops);