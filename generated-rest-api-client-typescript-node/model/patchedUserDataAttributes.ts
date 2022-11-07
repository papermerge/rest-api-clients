/**
 * Papermerge REST API
 * Document management system designed for digital archives
 *
 * The version of the OpenAPI document: 2.1.0b12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';
import { Permission } from './permission';

export class PatchedUserDataAttributes {
    /**
    * Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
    */
    'username': string;
    'firstName'?: string;
    'lastName'?: string;
    'email'?: string;
    /**
    * Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
    */
    'isActive'?: boolean;
    /**
    * Designates whether the user can log into this admin site.
    */
    'isStaff'?: boolean;
    /**
    * Designates that this user has all permissions without explicitly assigning them.
    */
    'isSuperuser'?: boolean;
    'dateJoined'?: Date;
    'userPermissions'?: Array<Permission>;
    'permCodenames'?: Array<string>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "username",
            "baseName": "username",
            "type": "string"
        },
        {
            "name": "firstName",
            "baseName": "first_name",
            "type": "string"
        },
        {
            "name": "lastName",
            "baseName": "last_name",
            "type": "string"
        },
        {
            "name": "email",
            "baseName": "email",
            "type": "string"
        },
        {
            "name": "isActive",
            "baseName": "is_active",
            "type": "boolean"
        },
        {
            "name": "isStaff",
            "baseName": "is_staff",
            "type": "boolean"
        },
        {
            "name": "isSuperuser",
            "baseName": "is_superuser",
            "type": "boolean"
        },
        {
            "name": "dateJoined",
            "baseName": "date_joined",
            "type": "Date"
        },
        {
            "name": "userPermissions",
            "baseName": "user_permissions",
            "type": "Array<Permission>"
        },
        {
            "name": "permCodenames",
            "baseName": "perm_codenames",
            "type": "Array<string>"
        }    ];

    static getAttributeTypeMap() {
        return PatchedUserDataAttributes.attributeTypeMap;
    }
}
