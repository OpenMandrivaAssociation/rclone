%global debug_package %{nil}

%bcond_without bootstrap2

# Run tests in check section
%bcond_with check

# https://github.com/rclone/rclone
%global goipath		github.com/rclone/rclone
%global forgeurl	https://github.com/rclone/rclone
Version:		1.71.1

%gometa

Summary:	Rsync for cloud storage
Name:		rclone

Release:	1
Source0:	https://github.com/rclone/rclone/archive/v%{version}/rclone-%{version}.tar.gz
%if %{with bootstrap2}
# Generated from Source100
Source3:	vendor.tar.zst
Source4:	go.sum
#Source100:	golang-package-dependencies.sh
%endif
URL:		https://github.com/rclone/rclone
License:	MIT AND BSD-3-Clause
Group:		Backup
BuildRequires:	compiler(go-compiler)
%if ! %{with bootstrap2}
#BuildRequires:	golang(bazil.org/fuse)
#BuildRequires:	golang(github.com/Azure/azure-sdk-for-go/sdk/azcore)
#BuildRequires:	golang(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
#BuildRequires:	golang(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
#BuildRequires:	golang(github.com/Azure/azure-sdk-for-go/sdk/storage/azfile)
#BuildRequires:	golang(github.com/Azure/go-ntlmssp)
#BuildRequires:	golang(github.com/Max-Sum/base32768)
#BuildRequires:	golang(github.com/Mikubill/gofakes3)
#BuildRequires:	golang(github.com/Unknwon/goconfig)
#BuildRequires:	golang(github.com/a8m/tree)
#BuildRequires:	golang(github.com/aalpar/deheap)
#BuildRequires:	golang(github.com/abbot/go-http-auth)
#BuildRequires:	golang(github.com/anacrolix/dms)
#BuildRequires:	golang(github.com/anacrolix/log)
#BuildRequires:	golang(github.com/atotto/clipboard)
#BuildRequires:	golang(github.com/aws/aws-sdk-go)
#BuildRequires:	golang(github.com/buengese/sgzip)
#BuildRequires:	golang(github.com/cloudsoda/go-smb2)
#BuildRequires:	golang(github.com/colinmarc/hdfs/v2)
#BuildRequires:	golang(github.com/coreos/go-semver)
#BuildRequires:	golang(github.com/coreos/go-systemd)
#BuildRequires:	golang(github.com/dop251/scsu)
#BuildRequires:	golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6)
#BuildRequires:	golang(github.com/gabriel-vasile/mimetype)
#BuildRequires:	golang(github.com/gdamore/tcell/v2)
#BuildRequires:	golang(github.com/go-chi/chi/v5)
#BuildRequires:	golang(github.com/go-git/go-billy/v5)
#BuildRequires:	golang(github.com/google/uuid)
#BuildRequires:	golang(github.com/hanwen/go-fuse/v2)
#BuildRequires:	golang(github.com/henrybear327/Proton-API-Bridge)
#BuildRequires:	golang(github.com/henrybear327/go-proton-api)
#BuildRequires:	golang(github.com/iguanesolutions/go-systemd/v5)
#BuildRequires:	golang(github.com/jcmturner/gokrb5/v8)
#BuildRequires:	golang(github.com/jlaffaye/ftp)
#BuildRequires:	golang(github.com/josephspurrier/goversioninfo)
#BuildRequires:	golang(github.com/jzelinskie/whirlpool)
#BuildRequires:	golang(github.com/klauspost/compress)
#BuildRequires:	golang(github.com/koofr/go-httpclient)
#BuildRequires:	golang(github.com/koofr/go-koofrclient)
#BuildRequires:	golang(github.com/mattn/go-colorable)
#BuildRequires:	golang(github.com/mattn/go-runewidth)
#BuildRequires:	golang(github.com/minio/minio-go/v7)
#BuildRequires:	golang(github.com/mitchellh/go-homedir)
#BuildRequires:	golang(github.com/moby/sys/mountinfo)
#BuildRequires:	golang(github.com/ncw/go-acd)
#BuildRequires:	golang(github.com/ncw/swift/v2)
#BuildRequires:	golang(github.com/oracle/oci-go-sdk/v65)
#BuildRequires:	golang(github.com/patrickmn/go-cache)
#BuildRequires:	golang(github.com/pkg/sftp)
#BuildRequires:	golang(github.com/pmezard/go-difflib)
#BuildRequires:	golang(github.com/prometheus/client_golang)
#BuildRequires:	golang(github.com/putdotio/go-putio/putio)
#BuildRequires:	golang(github.com/rfjakob/eme)
#BuildRequires:	golang(github.com/rivo/uniseg)
#BuildRequires:	golang(github.com/shirou/gopsutil/v3)
#BuildRequires:	golang(github.com/sirupsen/logrus)
#BuildRequires:	golang(github.com/skratchdot/open-golang)
#BuildRequires:	golang(github.com/spf13/cobra)
#BuildRequires:	golang(github.com/spf13/pflag)
#BuildRequires:	golang(github.com/stretchr/testify)
#BuildRequires:	golang(github.com/t3rm1n4l/go-mega)
#BuildRequires:	golang(github.com/willscott/go-nfs)
#BuildRequires:	golang(github.com/winfsp/cgofuse)
#BuildRequires:	golang(github.com/xanzy/ssh-agent)
#BuildRequires:	golang(github.com/youmark/pkcs8)
#BuildRequires:	golang(github.com/yunify/qingstor-sdk-go/v3)
#BuildRequires:	golang(go.etcd.io/bbolt)
#BuildRequires:	golang(goftp.io/server/v2)
#BuildRequires:	golang(golang.org/x/crypto)
#BuildRequires:	golang(golang.org/x/net)
#BuildRequires:	golang(golang.org/x/oauth2)
#BuildRequires:	golang(golang.org/x/sync)
#BuildRequires:	golang(golang.org/x/sys)
#BuildRequires:	golang(golang.org/x/text)
#BuildRequires:	golang(golang.org/x/time)
#BuildRequires:	golang(google.golang.org/api)
#BuildRequires:	golang(gopkg.in/validator.v2)
#BuildRequires:	golang(gopkg.in/yaml.v2)
#BuildRequires:	golang(storj.io/uplink)
#BuildRequires:	golang(cloud.google.com/go/compute)
#BuildRequires:	golang(cloud.google.com/go/compute/metadata)
#BuildRequires:	golang(github.com/Azure/azure-sdk-for-go/sdk/internal)
#BuildRequires:	golang(github.com/AzureAD/microsoft-authentication-library-for-go)
#BuildRequires:	golang(github.com/ProtonMail/bcrypt)
#BuildRequires:	golang(github.com/ProtonMail/gluon)
#BuildRequires:	golang(github.com/ProtonMail/go-mime)
#BuildRequires:	golang(github.com/ProtonMail/go-srp)
#BuildRequires:	golang(github.com/ProtonMail/gopenpgp/v2)
#BuildRequires:	golang(github.com/PuerkitoBio/goquery)
#BuildRequires:	golang(github.com/akavel/rsrc)
#BuildRequires:	golang(github.com/anacrolix/generics)
#BuildRequires:	golang(github.com/andybalholm/cascadia)
#BuildRequires:	golang(github.com/beorn7/perks)
#BuildRequires:	golang(github.com/bradenaw/juniper)
#BuildRequires:	golang(github.com/calebcase/tmpfile)
#BuildRequires:	golang(github.com/cespare/xxhash/v2)
#BuildRequires:	golang(github.com/cloudflare/circl)
#BuildRequires:	golang(github.com/cpuguy83/go-md2man/v2)
#BuildRequires:	golang(github.com/cronokirby/saferith)
#BuildRequires:	golang(github.com/davecgh/go-spew)
#BuildRequires:	golang(github.com/dustin/go-humanize)
#BuildRequires:	golang(github.com/emersion/go-message)
#BuildRequires:	golang(github.com/emersion/go-textwrapper)
#BuildRequires:	golang(github.com/emersion/go-vcard)
#BuildRequires:	golang(github.com/flynn/noise)
#BuildRequires:	golang(github.com/gdamore/encoding)
#BuildRequires:	golang(github.com/geoffgarside/ber)
#BuildRequires:	golang(github.com/go-ole/go-ole)
#BuildRequires:	golang(github.com/go-resty/resty/v2)
#BuildRequires:	golang(github.com/gofrs/flock)
#BuildRequires:	golang(github.com/gogo/protobuf)
#BuildRequires:	golang(github.com/golang-jwt/jwt/v5)
#BuildRequires:	golang(github.com/golang/protobuf)
#BuildRequires:	golang(github.com/google/s2a-go)
#BuildRequires:	golang(github.com/googleapis/enterprise-certificate-proxy)
#BuildRequires:	golang(github.com/googleapis/gax-go/v2)
#BuildRequires:	golang(github.com/hashicorp/errwrap)
#BuildRequires:	golang(github.com/hashicorp/go-multierror)
#BuildRequires:	golang(github.com/hashicorp/go-uuid)
#BuildRequires:	golang(github.com/hashicorp/golang-lru/v2)
#BuildRequires:	golang(github.com/inconshreveable/mousetrap)
#BuildRequires:	golang(github.com/jcmturner/aescts/v2)
#BuildRequires:	golang(github.com/jcmturner/dnsutils/v2)
#BuildRequires:	golang(github.com/jcmturner/gofork)
#BuildRequires:	golang(github.com/jcmturner/goidentity/v6)
#BuildRequires:	golang(github.com/jcmturner/rpc/v2)
#BuildRequires:	golang(github.com/jmespath/go-jmespath)
#BuildRequires:	golang(github.com/json-iterator/go)
#BuildRequires:	golang(github.com/jtolio/eventkit)
#BuildRequires:	golang(github.com/jtolio/noiseconn)
#BuildRequires:	golang(github.com/klauspost/cpuid/v2)
#BuildRequires:	golang(github.com/kr/fs)
#BuildRequires:	golang(github.com/kylelemons/godebug)
#BuildRequires:	golang(github.com/lucasb-eyer/go-colorful)
#BuildRequires:	golang(github.com/lufia/plan9stats)
#BuildRequires:	golang(github.com/mattn/go-isatty)
#BuildRequires:	golang(github.com/matttproud/golang_protobuf_extensions/v2)
#BuildRequires:	golang(github.com/minio/md5-simd)
#BuildRequires:	golang(github.com/minio/sha256-simd)
#BuildRequires:	golang(github.com/modern-go/concurrent)
#BuildRequires:	golang(github.com/modern-go/reflect2)
#BuildRequires:	golang(github.com/pengsrc/go-shared)
#BuildRequires:	golang(github.com/pkg/browser)
#BuildRequires:	golang(github.com/pkg/errors)
#BuildRequires:	golang(github.com/power-devops/perfstat)
#BuildRequires:	golang(github.com/prometheus/client_model)
#BuildRequires:	golang(github.com/prometheus/common)
#BuildRequires:	golang(github.com/prometheus/procfs)
#BuildRequires:	golang(github.com/rasky/go-xdr)
#BuildRequires:	golang(github.com/relvacode/iso8601)
#BuildRequires:	golang(github.com/rs/xid)
#BuildRequires:	golang(github.com/russross/blackfriday/v2)
#BuildRequires:	golang(github.com/ryszard/goskiplist)
#BuildRequires:	golang(github.com/shabbyrobe/gocovmerge)
#BuildRequires:	golang(github.com/shoenig/go-m1cpu)
#BuildRequires:	golang(github.com/sony/gobreaker)
#BuildRequires:	golang(github.com/spacemonkeygo/monkit/v3)
#BuildRequires:	golang(github.com/tklauser/go-sysconf)
#BuildRequires:	golang(github.com/tklauser/numcpus)
#BuildRequires:	golang(github.com/vivint/infectious)
#BuildRequires:	golang(github.com/willscott/go-nfs-client)
#BuildRequires:	golang(github.com/yusufpapurcu/wmi)
#BuildRequires:	golang(github.com/zeebo/blake3)
#BuildRequires:	golang(github.com/zeebo/errs)
#BuildRequires:	golang(go.opencensus.io)
#BuildRequires:	golang(golang.org/x/exp)
#BuildRequires:	golang(golang.org/x/mod)
#BuildRequires:	golang(golang.org/x/tools)
#BuildRequires:	golang(google.golang.org/appengine)
#BuildRequires:	golang(google.golang.org/genproto/googleapis/rpc)
#BuildRequires:	golang(google.golang.org/grpc)
#BuildRequires:	golang(google.golang.org/protobuf)
#BuildRequires:	golang(gopkg.in/ini.v1)
#BuildRequires:	golang(gopkg.in/yaml.v3)
#BuildRequires:	golang(storj.io/common)
#BuildRequires:	golang(storj.io/drpc)
#BuildRequires:	golang(storj.io/picobuf)
#BuildRequires:	golang(github.com/Microsoft/go-winio)
#BuildRequires:	golang(github.com/ProtonMail/go-crypto)
#BuildRequires:	golang(github.com/golang-jwt/jwt/v4)
#BuildRequires:	golang(github.com/golang/groupcache)
#BuildRequires:	golang(github.com/google/go-querystring)
#BuildRequires:	golang(github.com/pkg/xattr)
#BuildRequires:	golang(golang.org/x/mobile)
#BuildRequires:	golang(golang.org/x/term)
%endif

%description
Rclone ("rsync for cloud storage") is a command-line program
to sync files and directories to and from different cloud
storage providers.

%files
%license COPYING
%doc MAINTAINERS.md MANUAL.html RELEASE.md CONTRIBUTING.md MANUAL.md README.md
%doc docs/
%{_bindir}/%{name}
%{_bindir}/%{name}fs
%{_sbindir}/mount.%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completion/%{name}
# {_datadir}/fish-completion/completion{name}.fish
%{_datadir}/zsh-completion/completion/_%{name}

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

#-----------------------------------------------------------------------

%prep
export LC_ALL=C.utf-8
%autosetup -p1 -n rclone-%{version}
# After 1.69.2 go.sum throws checksum error. Deleting file and running go mod tidy recreates the go.sum file
rm -rf go.sum
# added go mod tiny to script
rm -rf vendor
cp %{S:4} %{builddir}


%if %{with bootstrap2}
tar xvf %{S:3}
%endif

%build
%gobuildroot
export LDFLAGS="-X github.com/rclone/rclone/fs.Version=%{version}"
%gobuild -o _bin/rclone %{goipath}
#for cmd in $(ls -1 cmd) ; do
#	#gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
#done

# completrions 
_bin/%{name} completion bash - > %{name}.bash
#_bin/%{name} completion fish - > %{name}.fish
_bin/%{name} completion zsh  - > %{name}.zsh

%install
#goinstall
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done

# manpage
install -Dpm 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1

# completions
install -Dpm 0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completion/%{name}
#install -Dpm 0644 %{name}.fish %{buildroot}%{_datadir}/bash-completion/completion/%{name}.fish
install -Dpm 0644 %{name}.zsh  %{buildroot}%{_datadir}/zsh-completion/completion/_%{name}

# https://rclone.org/commands/rclone_mount/#rclone-as-unix-mount-helper
	
install -Dpm 0755 -d %{buildroot}%{_bindir}
ln -rs %{buildroot}%{_bindir}/rclone %{buildroot}%{_sbindir}/mount.rclone
ln -rs %{buildroot}%{_bindir}/rclone %{buildroot}%{_bindir}/rclonefs

%check
%if %{with check}
%gochecks
%endif

